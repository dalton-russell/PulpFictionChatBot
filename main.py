#Dalton Russell
#11/1/2020
#This is a chatbot program
#It converses in a very limited scope about Pulp Fiction
#If a user makes it to the converse function, a text file will be created with their name
#The text file will contain whether or not they have seen the movie and everything that they input to the bot
#User input is then analyzed and written to a file named analyzed_text.txt
#This file contains information about user input including word frequencies
#This file could be used to train the bot better in the future

import nltk
import sys
from nltk.corpus import stopwords

#global variables
name = "None"
seen_movie = True
user_query = []
tokens = []
conversation = []

#analyze user input
def analyze():

    for item in user_query:

        # don't save 'seen movie' token
        if (item.__contains__("Seen movie") != True):
            tokenized_item = nltk.word_tokenize(item)
            for t in tokenized_item:
                tokens.append(t)

        # get rid of stopwords
        no_stopwords = [t for t in tokens if t not in stopwords.words('english')]

        # unique tokens
        unique_tokens = set(no_stopwords)

        # get a dictionary of token counts
        counts = {t: tokens.count(t) for t in unique_tokens}

        # sort dictionary
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        # get word frequencies
        frequencies = {t: "%.2f" % (tokens.count(t) / len(tokens) * 100) for t in unique_tokens}

        # sort frequencies
        sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

        # attempt to get subjects
        tags = nltk.pos_tag(unique_tokens)
        possible_subjects = [item for item, tag in tags if tag == 'NN']

    #save to text file
    with open('analyzed_input.txt', 'a') as filehandle:
        filehandle.write('\nUser name = ' + name + '\n')
        filehandle.write("Seen movie = " + str(seen_movie) + '\n')
        filehandle.write("\nToken counts: " + '\n')
        for key, value in sorted_counts:
            filehandle.write(str(key) + ' ' + str(value) + '\n')
        filehandle.write("\nPossible Subjects: " + '\n')
        for item in possible_subjects:
            filehandle.write(str(item) + '\n')
        filehandle.write("\nWord Frequencies: " + '\n')
        for key, value in sorted_frequencies:
            filehandle.write(str(key) + ' ' + str(value) + '\n')
        filehandle.write("--------------------")

#save user information and end program
#each user model is named after the user
def end():

    file_name = name + '.txt'

    #write all user input to text file
    with open(file_name, 'w') as filehandle:
        for item in user_query:
            filehandle.write('%s\n' % item)

    #analyze user input
    analyze()

    #end program
    sys.exit()

#function to build knowledge base of keys and values
def build_knowledge():
    knowledge = {
        'who directed': "Quentin Tarantino directed Pulp Fiction",
        'director': "Quentin Tarantino directed Pulp Fiction",
        'who wrote': "Quentin Tarantino and Roger Avary  wrote  Pulp Fiction",
        'writer':  "Quentin Tarantino and Roger Avary  wrote  Pulp Fiction",
        'tarantino': "Quentin Jerome Tarantino born March 27, 1963 is an American film director, screenwriter, producer, and actor. His films are characterized by nonlinear storylines, aestheticization of violence, extended scenes of dialogue, ensemble casts, references to popular culture and a wide variety of other films, soundtracks primarily containing songs and score pieces from the 1960s to the 1980s, alternate history, and features of neo-noir film.",
        'avary': 'Roger Roberts Avary born August 23, 1965 is a Canadian-American film and television director, screenwriter, and producer. He collaborated with Quentin Tarantino on Pulp Fiction, for which they won Best Original Screenplay at the 67th Academy Awards.',
        'award': 'Pulp Fiction won Best Original Screenplay at the 67th Academy Awards',
        'awards': 'Pulp Fiction won Best Original Screenplay at the 67th Academy Awards',
        'cast': 'The cast includes John Travolta, Samuel L. Jackson, Bruce Willis, Tim Roth, Ving Rhames, and Uma Thurman',
        'actors': 'The cast includes John Travolta, Samuel L. Jackson, Bruce Willis, Tim Roth, Ving Rhames, and Uma Thurman',
        'played jules': 'Samuel L. Jackson played Jules Winnfield',
        'plays jules': 'Samuel L. Jackson plays Jules Winnfield',
        'played vincent': 'John Travolta played Vincent Vega',
        'plays vincent': 'John Travolta plays Vincent Vega',
        'played marsellus': 'Ving Rhames played Marsellus Wallace',
        'plays marsellus': 'Ving Rhames plays Marsellus Wallace',
        'played mia': 'Uma Thurman played Mia Wallace',
        'plays mia': 'Uma Thurman plays Mia Wallace',
        'played butch': 'Bruce Willis played Butch Coolidge',
        'plays butch': 'Bruce Willis plays Butch Coolidge',
        'about jules': 'Jules Winnfield is the deuteragonist of Pulp Fiction. Initially he is a Hitman working alongside Vincent Vega but after revelation, or as he refers to it "a moment of clarity" he decides to leave to "Walk the Earth." During the film he is stated to be from Inglewood, California.',
        'about vincent': 'Vincent Vega is a hitman and associate of Marsellus Wallace. He is the protagonist of Pulp Fiction. He had a brother named Vic Vega who was shot and killed by an undercover cop while on a job. He worked in Amsterdam for over three years and recently returned to Los Angeles, where he has been partnered with Jules Winnfield.',
        'about marsellus': 'Marsellus Wallace is a gang boss and husband to Mia Wallace. He is the boss of Vincent Vega, Jules Winnfield, Butch Coolidge, and many other unknown gangsters. He is said to have thrown a man off a building for giving Mia a foot massage, and he is a victim of rape, courtesy of Zed.',
        'about mia': 'Mia Wallace is the new wife of Marsellus Wallace. She is a rather mysterious character, and very little is revealed about about her. She likes to wear elegant, expensive clothing, smokes cigaretes, enjoys music, and is addicted to cocaine.',
        'about butch': 'He is a tough southpaw boxer, but is nearing the end of his career, and is coerced into taking a bribe from mob boss Marsellus Wallace to throw the fight with Floyd Wilson.',
        'summary': 'Pulp Fiction is a 1994 American neo-noir black comedy crime film written and directed by Quentin Tarantino, who conceived it with Roger Avary. Starring John Travolta, Samuel L. Jackson, Bruce Willis, Ving Rhames, and Uma Thurman, it tells several stories of criminal Los Angeles.',
        'bible passage': 'The path of the righteous man is beset on all sides by the iniquities of the selfish and the tyranny of evil men. Blessed is he who in the name of charity and goodwill shepherds the weak through the valley of darkness, for he is truly his brothers keeper and the finder of lost children. And I will strike down upon thee with great vengeance and furious anger those who attempt to poison and destroy My brothers. And you will know My name is the Lord when I lay My vengeance upon thee.',
        'year': 'Pulp fiction released on October 14, 1994',
        'date': 'Pulp fiction released on October 14, 1994',
        'when': 'Pulp fiction released on October 14, 1994',
        'trivia': 'Marsellus and Mia never speak to one another on-screen, even though they are seen together poolside, and are husband and wife.',
        'jackson': 'Samuel L. Jackson played Jules Winnfield',
        'travolta': 'John Travolta played Vincent Vega',
        'thurman': 'Uma Thurman played Mia Wallace',
        'willis': 'Bruce Willis played Butch Coolidge',
        'rhames': 'Ving Rhames played Marsellus Wallace',
        'anything': 'Pulp Fictions narrative is told out of chronological order, and follows three main interrelated stories: Mob contract killer Vincent Vega is the protagonist of the first story, prizefighter Butch Coolidge is the protagonist of the second, and Vincents partner Jules Winnfield is the protagonist of the third.',
        'about': 'Jules Winnfield (Samuel L. Jackson) and Vincent Vega (John Travolta) are two hit men who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace (Ving Rhames). Wallace has also asked Vincent to take his wife Mia (Uma Thurman) out a few days later when Wallace himself will be out of town. Butch Coolidge (Bruce Willis) is an aging boxer who is paid by Wallace to lose his fight. The lives of these seemingly unrelated people are woven together comprising of a series of funny, bizarre and uncalled-for incidents.',
        'another fact': 'Much of Pulp Fictions action revolves around characters who are either in the bathroom or need to use the toilet.',
        'fact': 'Uma Thurman originally turned down the role of Mia Wallace. Quentin Tarantino was so desperate to have her as Mia, he ended up reading her the script over the phone, finally convincing her to take on the role.',
        'car': 'It was a 1964 Chevelle Malibu convertible',
        'did it make': 'It grossed over 200 million at the box office',
        'gross': 'It grossed over 200 million at the box office',
        'main character': 'Jules and Vincent are the main characters',
        'jules': 'Jules Winnfield is the deuteragonist of Pulp Fiction. Initially he is a Hitman working alongside Vincent Vega but after revelation, or as he refers to it "a moment of clarity" he decides to leave to "Walk the Earth." During the film he is stated to be from Inglewood, California.',
        'vincent': 'Vincent Vega is a hitman and associate of Marsellus Wallace. He is the protagonist of Pulp Fiction. He had a brother named Vic Vega who was shot and killed by an undercover cop while on a job. He worked in Amsterdam for over three years and recently returned to Los Angeles, where he has been partnered with Jules Winnfield.',
        'mia': 'Mia Wallace is the new wife of Marsellus Wallace. She is a rather mysterious character, and very little is revealed about about her. She likes to wear elegant, expensive clothing, smokes cigaretes, enjoys music, and is addicted to cocaine.',
        'butch': 'Butch is a tough southpaw boxer, but is nearing the end of his career, and is coerced into taking a bribe from mob boss Marsellus Wallace to throw the fight with Floyd Wilson.',
        'released': 'Pulp Fiction was released on October 14, 1994',
        'release': 'Pulp Fiction was released on October 14, 1994',
        }
    return knowledge

#start conversation
def converse():
    #flag to end conversation
    conversing = True

    #question to user
    print("What would you like to know about Pulp Fiction?")
    user_input = input()

    #save user input
    user_query.append(user_input)

    user_input = user_input.lower()

    no_answer = 0
    #conversation continues
    while (conversing == True):

        #found in dictionary keys
        found = False

        #end the conversation
        if (user_input == "bye" or user_input == 'nothing'):
            print("Goodbye " + name)
            if(seen_movie == False):
                print('I hope that you see Pulp Fiction some day')
            else:
                print('You should go watch Pulp Fiction again')
            end()

        #see if user input contains any keys from knowledge base
        for key, value in knowledge.items():
            if user_input.__contains__(key):
                print(knowledge[key])
                found = True
                break

        #input not found in knowledge base
        if(found != True):
            print("I'm sorry, I don't understand.")
            no_answer = no_answer+1
            if(no_answer % 2 == 0):
                print("My knowledge is somewhat limited")
                print("Some of the things I know are who played certain characters and information about them.")

        #get user input
        print('What else would you like to know?')
        user_input = input()

        # save user input
        user_query.append(user_input)

        user_input = user_input.lower()

#starting point
if __name__ == "__main__":

    #build dictionary of knowledge
    knowledge = build_knowledge()

    #first message from bot
    print("Hello, I can tell you about Pulp Fiction. You can end our conversation at any time by typing bye. What is your name?")
    user_input = input()

    #save user input
    user_query.append(user_input)


    user_input = user_input.lower()
    if (user_input == "bye"):
        print("Goodbye")
        sys.exit()

    #save user name
    #assumes name will come last in input
    #capitalize name
    user_input_list = user_input.split()
    name = user_input_list[-1].capitalize()

    print("Hello " + name)

    print("Have you seen Pulp Fiction?")
    user_input = input()

    # save user input
    user_query.append(user_input)

    user_input = user_input.lower()
    if (user_input == "bye"):
        print("That was fast. Goodbye then.")
        sys.exit()

    #user hasn't seen movie
    if(user_input.__contains__('no') or user_input.__contains__('na')):
        seen_movie = False
        print("Would you like to hear a summary?")
        user_input = input()

        # save user input
        user_query.append(user_input)

        user_input = user_input.lower()
        if (user_input == "bye"):
            print("Goodbye")
            sys.exit()
        if(user_input.__contains__('yes') or user_input == 'sure' or user_input == 'yeah' or user_input == 'ok'):
            print(knowledge['summary'])

    #continue conversation
    converse()
