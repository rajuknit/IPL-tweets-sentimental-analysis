follow these steps to see sentimental graph between two ipl teams.
1- Install python 2.7 on your system.
2- Install following package using pypi or pip
   	numpy
        scipy
        sklearn
        nltk 3.1
        pandas
        matplotlib     
3- Add sitecustomize.py from helper folder on "C:\Python27\Lib\site-packages\" directory and run it one time.
4- Download all necessary files for nltk by following command on cmd
    import nltk
    nltk.download()
5- Now run generate_pickles.py only one time.(NOTE- if you have pickled_algos folder than skip this step)
6- To show the live tweets sentimental analysis for a IPL team run livetweet_singleteam.py file and 
   livegraph_singleteam.py file simultaneously 
7- To compare live tweets sentimental analysis for two IPL teams run livetweet_twoteam.py file and 
   livegraph_twoteam.py file simultaneously.