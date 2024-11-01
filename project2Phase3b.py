
from mp_parsing_algorithms import ParseDatabase, generte_user_set, generate_movie_set, generte_ratings_set
from mp_parsing_algorithms import generate_genre_set, generate_ratings_set, generate_ratings_database
from mp_math_algorithms import calculate_per_genre_ratings_ratios_byGenre, rmse
from mp_accessory_algorithms import extract_from_list
from mp_visualization_algorithms import create_whisker_plot
from mp_visualization_implementation import visualize_gender_rating_data
from typing import List



#USAGE: RETURN A PARTITIONED DATA STRUCTURE WHICH SEGREGATES A TRAINING SET FROM A TESTING SET, GIVEN A SPECIFIED PERCENTAGE
def partitionRatings(rawRatings, testPercent):
    import random
    #this variable will indicate the number of randomly selected tuples to be present in the testing set.
    partition_Size = int(len(rawRatings)*(testPercent/100))
    #list will hold the random selections for the testing set
    t_set_indicies = {x:0 for x in random.sample(range(len(rawRatings)), partition_Size)}
    #the test set consists of the randomly selected tuples per indexes in  't_set_indicies'
    testSet = [rawRatings[x] for x in t_set_indicies]
    #the training set consists of all remaining tuples
    trainingSet = [ rawRatings[x] for x in range(len(rawRatings)) if x not in t_set_indicies]
    #return resultant data structures

    return [trainingSet, testSet]

#USAGE: GENERATE LIST OF PREDICTIONS FOR THE 5 ALGORITHMS
def generateAlgorithmicPredictions(data_set, rLu, rLm, userList, movieList):
    #list of true ratings
    actual_ratings = []
    #will provide a list of values for each algorithm implementation
    algorithm_predictions = [[] for x in range(9)]
    friends = {}
    #Where data_set[2] serves as the testing set
    for data in data_set:
        if not (data[0] in friends):
            friends[data[0]] = kNearestNeighbors(data[0],rLu,len(rLu))
        
        #true rating
        actual_ratings.append(data[2])
        #algorithm 1
        algorithm_predictions[0].append(randomPrediction(data[0], data[1]))
        #algorithm 2
        algorithm_predictions[1].append(meanUserRatingPrediction(data[0], data[1], rLu))
        #algorithm 3
        algorithm_predictions[2].append(meanMovieRatingPrediction(data[0], data[1], rLm))
        #algorithm 4
        algorithm_predictions[3].append(demRatingPrediction(data[0], data[1], userList, rLu))
        #algorithm 5
        algorithm_predictions[4].append(genreRatingPrediction(data[0], data[1], movieList, rLu))
        #algorithm 6
        algorithm_predictions[5].append(CFRatingPrediction(data[0], data[1], rLu, friends[data[0]][:10]))
        #algorithm 7
        algorithm_predictions[6].append(CFRatingPrediction(data[0], data[1], rLu, friends[data[0]][:100]))
        #algorithm 8
        algorithm_predictions[7].append(CFRatingPrediction(data[0], data[1], rLu, friends[data[0]][:500]))
        #algorithm 9
        algorithm_predictions[8].append(CFRatingPrediction(data[0], data[1], rLu, friends[data[0]]))
        
    return actual_ratings, algorithm_predictions
#USAGE: FUNCTION TAKES THE TEMPLATED ALGORITHMS AND PRODUCES 'DEGREE' NUMBER OF RESULTS VIA CROSS-VALIDATION (RATIO-> TEST_CLASSSIZE%)
def precisionTesting(degree, test_classSize):
    #load data structures
    userList = createUserList()
    movieList = createMovieList()
    ratingTuples = readRatings()

    i = 0
    #Extract per algorithm data
    algorithm_data = [[] for x in range(9)]
    while (i < degree): 
        #print('iteration ', i)
        #create a partition of training set and testing set
        data_set = partitionRatings(ratingTuples, test_classSize)
        #print('data set partitioned')
        #where data_set[0] serves as the training set, create a rLu and rLm which regards to the training set.
        training_set = createRatingsDataStructure(len(userList), len(movieList), data_set[0])
        #print('training set created')
        #Produce algorithmic predictions and actual ratings
        actual_ratings, algorithm_predictions = generateAlgorithmicPredictions(data_set[1], training_set[0], training_set[1], userList, movieList)
        #print('predictions produced')
        result = (generateRMSEValues(actual_ratings, algorithm_predictions))
        #print('rmse values produced')
        algorithm_data[0].append(result[0])
        algorithm_data[1].append(result[1])
        algorithm_data[2].append(result[2])
        algorithm_data[3].append(result[3])
        algorithm_data[4].append(result[4])
        algorithm_data[5].append(result[5])
        algorithm_data[6].append(result[6])
        algorithm_data[7].append(result[7])
        algorithm_data[8].append(result[8])
        i = i + 1
    
    #Return testing results   
    return algorithm_data

#USAGE: RETURNS LIST OF RMSE VALUES 
def generateRMSEValues(actual_ratings, predictions):
    #Returns a list of calculated RMSE Values of size 1 or greater
    output = []
    #For each set of predictions
    for algorithm in predictions:
        #calculate the RMSE value
        output.append(rmse(actual_ratings, algorithm))    
    
    return output




#MAIN
########################################MAIN########################################################################################
algorithm_data = precisionTesting(10, 20)
create_whisker_plot(algorithm_data, "Project2Phase3Plots")
###########################END MAIN#################################################################################################
labels = ('Action', 'Comedy', 'Drama', 'Horror',  'Romance')
