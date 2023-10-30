import re

# Define the predefined rules and responses
rules = {
    'hello': 'Hello! How can I help you ?',
    'drama korean': ' Yes, sure i have more Suggestions like : \n 1- the voice \n 2- investigation couple \n 3- taxi driver \
                    \n 4- shadow detective \n 5- Mouse \n 6- item \n 7- secret forest',

    'goodbye': 'Goodbye! Have a great day!',
    'name': 'My name is Chatbot. Nice to meet you!',
    'default': 'I\'m sorry, but I didn\'t understand your query. Could you please rephrase it?',

    # drama
    'the voice' : ''' Voice (Korean: 보이스); It is a television series consisting of 4 seasons. 
                The series premiered on January 14, 2017. The first season concluded on March 12. 
                The second season aired from August 11 to September 16, 2018.
                The third season aired from May 11 to June 30, 2019. 
                The fourth season aired from June 18 to July 31, 2021 
                The drama talks about a special team in the police unit formed by police officer Lieutenant Kang Kwon Joo (Lee Hana), 
                which includes many experienced individuals. The goal of the first team is to deal with the most brutal crimes and catch the unknown dead.
                for more information check this web  ( https://en.wikipedia.org/wiki/Voice_(TV_series)  ) ''',

    'investigation couple': '''  Investigative Couple or Partners for Justice (Korean: 검법남녀; RR: Geombeomnamnyeo) is a two-season South Korean television series.
                                 The first in 2018
                                 The second is in 2019
                                 The series revolves around the forensic doctor, Baek Beom, who is skilled at his job but has an eccentric personality, and the prosecutor, Eun Seol, a rookie prosecutor with a warm heart.
                                 She has a bright personality and comes from a wealthy family background. They come to work together to solve cases.
                                 For more information, see this web (https://en.wikipedia.org/wiki/Partners_for_Justice) ''',

    'taxi driver': ''' Taxi Driver (Korean: 모범택시) is a two-season South Korean television series starring Lee Ji-hoon, Kim Eui-sung, Pyo Ye-jin, Jang Hyuk-jin, and Bae Yeo-ram with Isom in the first season and Shin Jae-ha in the second season.
                       The first season premiered April 2021,
                       The second season premiered in February 2023,
                       The series is inspired by a real-life heinous crime committed in Korea. The series received praise from viewers for its performances and stories
                       for more information check this web  ( https://en.wikipedia.org/wiki/Taxi_Driver_(South_Korean_TV_series) ) ''',

    'shadow detective': ''' Shadow Detective (Korean: 형사록); It is a South Korean web series, starring Lee Seung Min, Jin Goo, Kyung Soo Jin, and Lee Hak Joo.
                            The first season premiered in 2022
                            The second season will premiere in 2023.
                            The series revolves around Kim Taek-rok (Lee Seung-min), a veteran investigator at the Jaimu Police Station. 
                            He is waiting for his retirement. Meanwhile, Kook Jin Han (Jin Woo) is transferred to Jaemu Police Station as head of the investigation team where Kim Taek Rok works. 
                            One day, Kim Taek Rok receives a phone call. The caller tells him he is an old friend. 
                            Thus begins his mysterious phone calls. In a call, he also tells him that he killed their colleague Woo Hyun-seok. 
                            Kim Taek-rok soon becomes a suspect in Woo Hyun-seok's murder. The caller suggests that they should look into Kim Taek Rok's past to find the things he did wrong. 
                            At first, Kook Jin Han suspected Taek Rok of being the killer in Woo Hyun-seok's death, but eventually he began to trust Taek Rok and his innocence. 
                            They begin searching for Taek Rok's old friend with the help of investigators Song Ah (Kyung Soojin) and Son Kyung Chan (Lee Hak-joo).
                            for more information check this web  ( https://ar.wikipedia.org/wiki/%D9%85%D8%AD%D9%82%D9%82_%D8%A7%D9%84%D8%B8%D9%84 ) ''',

    'mouse': ''' Mouse (Korean: 마우스; RR: Mauseu) is a South Korean erotic television series starring Lee Hye Joon,
                 Lee Seung Gi, Park Joo Hyun, and Kyung Soo Jin. The series is directed by Choi Jun-bae and Kang. 
                 Cheol-woo and written by Choi Ran, follows traumatized detective Go Mu-Chi (Lee Hee-joon) and his young colleague Jeong Ba-reum (Lee Seung-gi) as they hunt down a serial killer.
                 It premiered in 2021 
                 for more information check this web  ( https://en.wikipedia.org/wiki/Mouse_(TV_series) )''',
    'item': ''' Item (Korean: 아이템; RR: Aitem) is a 2019 South Korean television series.
                The series revolves around a prosecutor and a criminal analyst working together in their attempts to decipher the secrets of various mysterious items that have special powers.
                for more information check this web  ( https://en.wikipedia.org/wiki/Item_(TV_series)  ) ''',
    'secret forest': '''  secret forest or  Stranger (Korean: 비밀의 숲) is a two-season South Korean crime suspense drama television series, 
                          The first season of which premiered in 2017.
                          The second season, which premiered in 2020.
                          In the first season, Hwang Si Mok (Cho Seung Woo) is an executive prosecutor who suffers from hypersensitivity to certain sound frequencies.
                           After undergoing corrective surgery, he has lost his sense of empathy and lacks social skills. 
                           While investigating a murder, he meets police lieutenant Han Yeo-jin (Bae Doona), who helps him solve the case. 
                          As they begin to unravel the mystery behind the murder, they find that their efforts are constantly obstructed by participants in a major corruption conspiracy between the district attorney's office and a private conglomerate.
                          In the second season, set two years later, a conflict arises between the Public Prosecutor's Office and the National Police Agency, as the former wants to control all investigative procedures while the latter seeks independent authority to conduct investigations. 
                          In the midst of conflict between their agencies, Hwang Si Mok and Han Yeo Jin team up to conduct their own independent investigation into a hidden case. 
                         for more information check this web  ( https://en.wikipedia.org/wiki/Stranger_(TV_series)  ) ''',

     ###

}

# Define a function to process user queries
def process_query(query):
    query = query.lower()  # Convert the query to lowercase for case-insensitive matching

    # Check if the query matches any predefined rules
    if re.search(r'hello', query):
        return rules['hello']

    elif re.search(r'drama korean', query):
        return rules['drama korean']

    elif re.search(r'the voice', query):
        return rules['the voice']

    elif re.search(r'investigation couple', query):
        return rules['investigation couple']

    elif re.search(r'taxi driver', query):
        return rules['taxi driver']

    elif re.search(r'shadow detective', query):
        return rules['shadow detective']

    elif re.search(r'mouse', query):
        return rules['mouse']

    elif re.search(r'item', query):
        return rules['item']

    elif re.search(r'secret forest', query):
        return rules['secret forest']

    elif re.search(r'goodbye', query):
        return rules['goodbye']
    elif re.search(r'name', query):
        return rules['name']

    else:
        return rules['default']

# Chatbot interaction loop
while True:
    user_input = input("User: ")  # Get user input
    response = process_query(user_input)  # Process the user query
    print("Chatbot:", response)  # Print the chatbot's response

    if user_input.lower() == 'goodbye':
        break  # Exit the loop if user says goodbye

