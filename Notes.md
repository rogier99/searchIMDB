# Approach
For this assignment a few requirements are given. Use this library (cinemagoer) and create some features.
My first step would involve finding out the features already provided by the library, some functions might already be implemented, and given the time contrained, to create a mockup like this such features are quick to implement.
This involves reading guides and going through the documentation to find out what functions are available.

# Assumptions
My assumption would be that the code provided by the library is well optimised, such that, in most cases they do not need to changed to be optimal in our usecase.
The dataset provided by the library is also sound, and when using functions provided by the library I should not expect any bugs.
Whilst this is often not the case, creating a perfect piece of code is nearly impossible, it is out of my scope to account for them unless that becomes part of the project.

# Tools
There are a few categories of tools to choice.

## Editor
During university I often used vim to program.
This editor does not provide auto complete or other fancy tools, but is very powerfull as almost any feature can be implemented and most importantly is supported on almost any device.
For some assignments and especially duing corona using the terminal to program was often desired so vim was an excelent tool.
If I were to use this more, one of the first things I would do is try and implement these features as they reduce the effective programming time and can provide hints for what functions are available and their application.
It is more likely I will simply switch to another editor that provides auto complete amongst other features, but this is up to debate.

## Testing
For my assignements the tests were always hand made, and executed.
I did not use github features for those as it would a lot of work for a relative small assignment.
However when a project goes for longer than a half a year and include more than 3 people these automated tests become important and the time invested to implement them is validated.

## Others
I have yet to use other tools as well.
For the most part when implementing something the only worries are editors, testing environments and the libraries used.

# Orginisation
To ensure everyone involved can access the files I often use github.
It is an excelent platform to share files, keep track of changes, allow branching and merging allowing for parallel programming and many other features.
I would seperate the work by features and share them amongst other developers such that there is minimal overlap.
In most cases there will be some overlap which is why I would like all parties involved to prepare a list of requirements that can be shared with the others.
This could be requesting a function with set inputs, executing and output, so that their part can simply assume this works and focus on implementing everything else.
When reviewing it is important that someone else looks at the code, preferable someone who is using these features as they will know what the program does without knowing how this is achieved.
In case something is wrong or simply unclear they will more likely be able to provide constructive featback.

# Structure
It is important that there is a good balance between file amount and file size.
Clustering all features in a single file will make the readablity weak, too much text to sift through with limited originisation.
However creating a new file for every function will make navigation slow.
A single function often uses more than 10 others, this using 10 files, with is for both the user trying to find bugs and the compiler trying to fetch instructions very slow.
In practice features often shape in trees, where functions on  a higher level only use fuctions below itself and are often clustered by catagory.
We may have search bar with many possible answeres, and movies may only be a small part.
Movies may get their own folder with associated files and folders seperating file types and functions, like API's and tests.

## Naming
For naming files, functions and variable I only care about consistency.
In most cases these things are very similar (camelCase and such).
The names themselves should be as short as possible whilst providing sufficient information.
Using numbers or otherwise unclear multiples of variables will be confusing and resulting in mistakes.
Variables should be at max two words, whilst functions and files can go up to 5 words each.

## Documentation
For documentation it is important that a baseline is provided.
Some tutorials on basic features can aid starting with the library.
I personally also want a list of all the features, given a class or type, what does it contain (integers, bools, strings) and what functions are available.
For every function; what are all the required and optinal variables and how are they contraint, what does the function do on a higher level and how is the state of the program changed, and finally what is the output/returned by the program.

# Maintanance
In order to maintain the program as it is running, it is important that the program is modular, every feature is seperated and can be used anywhere, has enough comments such that an outsider can figure out what the function does and is well documented.
Automated tests are important to ensure that all the involved features are still working and with every added feature the test should be extended.
When librarys are updated it is important to keep a back-up (which is alread provided by github) and run all tests affected by this update again.
In some cases the library only adds features, so using an outdated version is fine, however when the library gets faster and/or more secure it will be important to find and fix bugs caused by the update as that will be important tof the continuation of the program.
Using seperate branches in github is ideal as you can upload any changes made without rolling them to production such that you can again rollback in case some mistakes are made.
