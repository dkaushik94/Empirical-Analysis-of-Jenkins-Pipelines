# Empirical Analysis of Jenkins Pipelines

The primary aim of this project is to discover patterns and trends in various repositories and their continuous integration pipelines. We saw that the settings for different repositories and their intrinsic properties are related to their corresponding continuous integration pipeline settings. The scope of the project itself is huge due to the various types of co*routines and tasks available to be performed in automated testing processes. We analyzed groovy syntax and extracted stages, shell script commands, build invocations using different build tools used.

# Run this project

To run the project make sure you have all the libraries nad dependencies. To do this run 
`pip3 install *r Requirements.txt`.

This will install all required libraries. 
* PyGal
* Plotly
* Keras
* scikit*learn
* wordcloud
* NumPy
* Pandas
* Seaborn

Run `python3 Jenkins_analyzer.py` to initiae the script and it will run the complete analysis and generate the following files in the root directory.
* build_tools.svg
* stages_word_cloud.png
* stages_word_cloud_low_level.png
* cluster_n.png (30 files)

**Log file** includes all the log messages while running the system.

## Report
The repository contains our finding and a complete report which is contains all the details of the project. The file name is *'EAJP_report.pdf'*

## Tests
To run the tests, run the python file `python3 Statistics_test.py`

## Repository Data
We already have jenkinsfiles in the repository. We have fetched it using the script. Run the command `python3 Repositories.py` to download all the repositories.

## Contributors:
* Debojit Kaushik (https://dkaushik94.github.io, dkaush4@uic.edu)
* Sandeep Joshi (sjoshi37@uic.edu)

## References:
Some of the libraries and references with want to mention:
* PyGal
* Plotly
* Keras
* Numpy
* Pandas
* Seaborn
* scikit*learn
* [Jenkins Documentation](https://jenkins.io/doc/book/pipeline/syntax/)
* www.python.org 
* wordcloud (Python Library) 
* overleaf (Collaborative LaTex editor)
* www.draw.io
* [Dr. Mark Grechanik](https://www.cs.uic.edu/~drmark/)


*Note: This project was a part of CS540: Adv Techniques in Software Engineering for the semester of Spring'18 at the University of Illinois at Chicago.*