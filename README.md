                                      Project Report - Programming Language (CS-306)

                                                  (Code Quality Analyzer)

Aim -> To analyze how readable is the code.

Project Description -> We have build a tool named Linter that will give a score to a given code based on the following parameters.

1. Line Length
2. Indentation
3. No. of Comments
4. No. of Blank Lines 
5. Length of Functions

For every parameter, a function is created to test and score the code.

Approach -> The entire code is taken as an array of strings. Each line is checked one by one by different Regular Expressions. We have created Regex for different functions that adhere to some guidelines set by the Google in the Google C++ style guide and cpplint.

Conclusion/Future Scope –> After running the code, it outputs the respective scoring in each
parameter as well as a detailed report on what went wrong in each line.
With extra time, the rules for scoring could be made more robust. Also we can add other parameters like checking the scope of the variables, etc.


Team Members-

  Ankit Gahlawat(IMT2015010), 
  Udit Jindal(IMT2015043), 
  Rohil Pal(IMT2015520)
 
