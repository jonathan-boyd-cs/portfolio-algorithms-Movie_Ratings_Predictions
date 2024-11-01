# A Movie Ratings Prediction Application
## University of Iowa Computer Science Project ( created : Spring 2023 ) ( refactored : 2024 Nov 1)
## Author : Jonathan Boyd
This project involves parsing a database of movie ratings information. The database consists of 100,000 ratings, having given rise to the task of efficiently extracting such data and calculating rating predictions in various manners. Algoirithms such as KNearestNeighbors, MergeSort, RMSE, and Pearson's correlation coeffiencet are utilized. The assignment left ample room to accidentally build a program which ran an entire night.<br>
The implementation has been refactored into various well-named components. Mathematical functions are implemented, as are accessories and visualizations. The parsing is tailored to the dataset formats. The predictive algorithms are well explained through documentation; as always in my style, written such that hovering in VSCode allows easy reading of a functions mode of action. The testing suite provides a well tailored data aquisition function, allowing for plotting various forms of the data. The example outputs illustrate one of many ways to view the results. It has been noted that omitting various results might yield more formitable scaling.<br>
### How to run the programs
To run the programs...<br>
<ol>
    <li>prediction_algorithm_comparisons.py</li>
    <li>ratings_data_visualization.py</li>
</ol><br>
simply type at the command line : <code>python3 (module)</code>
<br>

### Notes
- The prediction_algorithm_comparisons.py program appears to manage 10 test iterations in 4 minutes. Reducing the degree to 5 effectively halves this time to 2 minutes. It would be a great pleasure if breakthroughs for faster code were discovered.
- There is chance that more work will be don on the programs objects in the future.
