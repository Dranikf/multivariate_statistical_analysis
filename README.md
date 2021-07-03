# multivariate_statistical_analysis
including labs and home works that i did in education process

# Lab1
3 dimentional discriminant analysis for given data.
black surface is disctiminant funciton plot.
blue surcles is data range 1, orange triangles is data range 2.
big markers shows positions of object with undefined group.
<img src = "https://github.com/Dranikf/multivariate_statistical_analysis/blob/main/lab1/result_plot.png" height = "600">

# Lab2
transforming the original data system using the principal components method. 
eliminates autocorrelation in the data. For example transforming of some dataset

<img src = "https://github.com/Dranikf/multivariate_statistical_analysis/blob/main/lab2/result.png" height = "200">

# Lab3
visualisation of sphere with points

<img src = "https://github.com/Dranikf/multivariate_statistical_analysis/blob/main/lab3/result.png" height = "200">

# Lab4
example of diskriminant analysis for 3 samples
visualisation of input data

<img src = "https://github.com/Dranikf/multivariate_statistical_analysis/blob/main/lab4/hello.png" height = "600">

for every sample there is separate funciton - for new points (big red points) computes values of funcitons. function with bigest value represent the most close sample.
and result will be like that. 

<img src = "https://github.com/Dranikf/multivariate_statistical_analysis/blob/main/lab4/result.png" height = "200">

# independent work (ysrs1)

its for cluster analysis - there is some partition functions - characterize the quality of this or that partition.
for cluster analysis, we need to choose a functional, and calculate it for all possible partitions.
First, we get the partitions
function theory/combinator.py - works for this purpose. For example objects [1,2,3,4,5,6], clusters [2,3,1]
combinations will look like: 

then objects are selected according to the different partitions and substituted in the partition functionals.
funcionals can be founded in lab/compute_functionals.py.
example in main notebook. this is partition with best funcitonal value for two equal clusters.

<img src = "https://github.com/Dranikf/multivariate_statistical_analysis/blob/main/mmsa%20ysrs1%20klaster%20combin/lab/plot1.png" height = "600">