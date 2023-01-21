import cohere
from cohere.classify import Example

def get_start_class(response: str) -> str:
    examples = [Example("I don\'t care", "negative"),
                Example("go to hell", "negative"),
                Example("don\'t be a coward", "negative"),
                Example("you petty little bitch", "negative"),
                Example("why so rude", "neutral"),
                Example("But that\'s not my fault", "neutral"),
                Example("where\'s the classroom", "neutral"),
                Example("thank you very much", "positive"),
                Example("I really appreciate it", "positive"),
                Example("I like your dress", "positive"),
                Example("you did good", "positive"),
                Example("The order came 5 days early", "positive"),
                Example("The item exceeded my expectations", "positive"),
                Example("I ordered more for my friends", "positive"),
                Example("I would buy this again", "positive"),
                Example("I would recommend this to others", "positive"),
                Example("The package was damaged", "negative"),
                Example("The order is 5 days late", "negative"),
                Example("The order was incorrect", "negative"),
                Example("I want to return my item", "negative"),
                Example("The item\'s material feels low quality", "negative"),
                Example("The product was okay", "neutral"),
                Example("I received five items in total", "neutral"),
                Example("I bought it from the website", "neutral"),
                Example("I used the product this morning", "neutral"),
                Example("The product arrived yesterday", "neutral")]
    co = cohere.Client('mDgdZhuZohzzJnVmOnygreJzaxHyvUD4MdPcEoOq')

    #print(
    #    f"OK, you said \" {response} \"  Let's see if this is a good response.")

    response_class = co.classify(
        model='large',
        inputs=[response],
        examples=examples,
    )

    sentence = str(response_class.classifications[0])
    result = sentence.index('prediction: ')
    result_class = sentence[result + 13: result + 21]
    return result_class

def get_class(response: str) -> str:
    examples = [Example("I don\'t care", "negative"),
                Example("go to hell", "negative"),
                Example("don\'t be a coward", "negative"),
                Example("you petty little bitch", "negative"),
                Example("why so rude", "neutral"),
                Example("But that\'s not my fault", "neutral"),
                Example("where\'s the classroom", "neutral"),
                Example("thank you very much", "positive"),
                Example("I really appreciate it", "positive"),
                Example("I like your dress", "positive"),
                Example("you did good", "positive"),
                Example("The order came 5 days early", "positive"),
                Example("The item exceeded my expectations", "positive"),
                Example("I ordered more for my friends", "positive"),
                Example("I would buy this again", "positive"),
                Example("I would recommend this to others", "positive"),
                Example("The package was damaged", "negative"),
                Example("The order is 5 days late", "negative"),
                Example("The order was incorrect", "negative"),
                Example("I want to return my item", "negative"),
                Example("The item\'s material feels low quality", "negative"),
                Example("The product was okay", "neutral"),
                Example("I received five items in total", "neutral"),
                Example("I bought it from the website", "neutral"),
                Example("I used the product this morning", "neutral"),
                Example("The product arrived yesterday", "neutral")]
    co = cohere.Client('mDgdZhuZohzzJnVmOnygreJzaxHyvUD4MdPcEoOq')

    print(
        f"OK, you said \" {response} \"  Let's see if this is a good response.")

    response_class = co.classify(
        model='large',
        inputs=[response],
        examples=examples,
    )

    sentence = str(response_class.classifications[0])
    result = sentence.index('prediction: ')
    result_class = sentence[result + 13: result + 21]
    return result_class


def reasonable_answer(class_start: str, class_response: str) -> str:
    if class_start == class_response:
        print(f"Your response is {class_response}, "
              f"same as the speaker, this is reasonable.")
    else:
        if class_start == "negative" and class_response == "positive":
            print(f"You are too kind")
        elif class_start == "negative" and class_response == "neutral\"":
            print(f"You are a little too kind")
        elif class_start == "positive" and class_response == "negative":
            print(f"You are a little too mean")
        elif class_start == "positive" and class_response == "neutral\"":
            print(f"You are a little too mean")
        elif class_start == "neutral\"" and class_response == "positive":
            print(f"You are kind! Good job.")
        elif class_start == "neutral\"" and class_response == "negative":
            print(f"You can be more negative")


if __name__ == '__main__':
    start_sentence = "You can’t even get that answer? You’re so dumb!"
    print("You can’t even get that answer? You’re so dumb!")
    class_start = get_start_class(start_sentence)

    response = input("Enter your response: ")
    result_class = get_class(response)
    print("Your response is", result_class)

    reasonable_answer(class_start, result_class)
