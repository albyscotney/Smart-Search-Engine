# ST101 Programming for Data Science

## Objectives

The project serves as the most important coursework for us to assess your progress in the course in terms of:
* Understanding of the course materials
* Ability to apply the course materials on real life problems using programming
* Other skills like self learning skills

To allow us to be able to assess the qualities above, you are asked to complete three programming tasks and write a report to show your results (See the section `Tasks` for more details). You are also required to use the programming concepts/tools listed under the section `Concepts/tools you must use` to show that you are capable of applying _all_ the programming concepts/tools we have learned in this course.

---

## Tasks

In the project, we will continue working on the Netflix example we have been working on with problem set 8 and 9. In the previous problem sets, we have done the following:

* Write the class `StreamingService` and `Playlist` to represent some streaming services and playlists
* Investigate what an efficient way is to get the details of a show given the name of the show

While the problem sets were inspired by the real world problem, they were highly simplified. For example, for the `Playlist` we assume different playlists (like "favourites", "history" or "watch later") will behave in the same way but in reality this is not the case. The search is also over simplified - we require users to provide the exact title of the show in order to be able to get the show details. In real life we seldom need to provide the exact terms to get a meaningful search result.

In the project, we consider more realistic situations on similar problems, and you are asked to do the following programming tasks:

1. Create the class `User` to represent the subscribers for a streaming service and add the class `FavouritePlaylist` so that we can have different types of playlists. See [user_and_playlist.md](user_and_playlist.md) for further instructions (25%)
2. Re-implement the searching method so that we have a smarter searching engine. See [serach_engine.md](search_engine.md) for further instructions (45%)
3. Do a performance analysis on (2) or data analysis on Netflix data. See [analysis.md](analysis.md) for further instructions (30%)

All the code must be submitted.

You are also required to write a report in a Jupyter Notebook to summarise your program and findings in the following structure:

1. Short introduction
    * What you are going to do in this project
2. Task 1
3. Task 2
4. Task 3
5. Conclusion and reflection
    * What you have done
    * What are the limitations
    * What can be improved (in terms of both implementation and analysis) or what other functionality you may want to add if you have more time and resources

For what you need to include in the report for task 1-3, please refer to the corresponding instructions.

---

## Concepts/tools you _must_ use

In order to get a high mark for the project, you _must_ use _all_ of the following in your project <ins>appropriately</ins>:

* Basics: control flow and containers
* Functions: abstraction and decomposition
* Modules: modularisation
* At least one library not demonstrated (but it can be _mentioned_) in the course
* Important data science tools including `Numpy` and/or `Pandas` (with vectorised operations) and `Jupyter Notebook`
* Good practice: testing, assertion, use of comments
* Error raising and handling
* Class: encapsulation, abstraction, composition, inheritance

See the marking criteria below for more details.

If you think that some concepts/tools above are not appropriate for what you want to do, please contact the lecturer and we will see if such omission can be accepted, or alternative arrangement can be made.

---

## Knowledge that you _may_ consider to demonstrate

* Algorithm analysis / actual running time comparison
* Simulation
* Parallel programming
* Programming paradigms
* Debugging


Note that it is not compulsory to use the tools listed in this section, although if you are aiming at a very high mark (>85), you may consider including some of them in your project.

---

## Data

The main data we will use is the [netflix_titles.csv](data/netflix_titles.csv) from Kaggle. For task 3, you may also want to use the IMDb data.

netflix_titles.csv has the following columns:

* type: Identifier - A Movie or TV Show
* title: Title of the Movie / Tv Show
* director: Director of the Movie
* cast: Actors involved in the movie / show
* country: Country where the movie / show was produced
* date_added: Date it was added on Netflix
* release_year: Actual Release year of the move / show
* rating: TV Rating of the movie / show
* duration: Total Duration - in minutes or number of seasons
* listed_in: Genre
* description: The summary description

We assume the titles of the show are unique in netflix_titles.csv.

---

## List of modules / libraries / data structure that you can use

You can use the tools below without the need of getting permission from the lecturer:

* `random` library and any of the functionality provided by it
* `multiprocessing` library and any of the functionality provided by it
* `datetime` and `time` library and any of the functionality provided by it
* `set` and any of the functionality provided by it
* `Pandas` and `Numpy`, but you can only use them for the tasks that specified that you can use them, or you use them for some "additional" / "optional" features, or you have got the approval from the lecturer
* `nltk` library

For any "optional" or "additional" functionality that you want to add, there is no restriction on what you can use.

For any other modules / libraries / data structure / unseen built-in methods that you want to use, please get the permission from the lecturer. Moodle will also keep a list of approved modules / libraries / data structure / unseen built-in methods so please have a look as well. You will be penalised if you are using unauthorised modules / libraries / data structure / unseen built-in functions, etc. in your project.

---

## Important information, please read

* _Unless_ you are told otherwise / you have got the permission from the lecturer / it is your own work / it is for some additional features, you are _not_ allowed to use
    * Modules
    * Libraries
    * Built-in functions (including methods) and types

that are _not_ covered or seen in the course
* Your submission must be 100% your own work. It means that (_unless_ you are told otherwise):
    * All the code must be written by yourself
    * You cannot reference to _any_ materials for the problem solving logic (e.g. you cannot try to search "how to use Python to build index")
    * You cannot discuss or communicate with your fellow classmates or any other people (except the lecturer) about the problem set before the hard deadline
    * You _may_ reference to answers for some _generic_ questions like "how to iterate over a dictionary", but it is safer to check with the lecturer if you are not sure about it
* We take plagiarism seriously. All the submitted code will be sent to an automatic system to determine the similarity. Any suspicious plagiarism will be reported for further investigation
* If you are not sure about the questions, please use the Moodle forum so that everyone else can know as well. Alternatively you can directly contact the lecturer
    * Please do not post your logic or any part of your answers on Moodle

---

## Note

* You have the freedom to decide many things for the project. For example, you can decide what to do if there is some missing data in the csv file. There is no right or wrong, but it should be sensible and clear to the person who is reading your report / using your code.
* Remember that you are required to use _all_ tools listed above
