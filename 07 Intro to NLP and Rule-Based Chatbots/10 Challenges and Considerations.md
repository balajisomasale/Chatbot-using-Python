# Challenges and Considerations
As you’ve seen, there are a vast array of applications for NLP. However, as they say, “with great language processing comes great responsibility” (or something along those lines). When working with NLP, we have several important considerations to take into account:

<li>Different NLP tasks may be more or less difficult in different languages. Because so many NLP tools are built by and for English speakers, these tools may lag behind in processing other languages. The tools may also be programmed with cultural and linguistic biases specific to English speakers.
</li><li>What if your Amazon Alexa could only understand wealthy men from coastal areas of the United States? English itself is not a homogeneous body. English varies by person, by dialect, and by many sociolinguistic factors. When we build and train NLP tools, are we only building them for one type of English speaker?
</li><li> You can have the best intentions and still inadvertently program a bigoted tool. While NLP can limit bias, it can also propagate bias. As an NLP developer, it’s important to consider biases, both within your code and within the training corpus. A machine will learn the same biases you teach it, whether intentionally or unintentionally.
</li><li>As you become someone who builds tools with natural language processing, it’s vital to take into account your users’ privacy. There are many powerful NLP tools that come head-to-head with privacy concerns. Who is collecting your data? How much data is being collected and what do those companies plan to do with your data?
## Instructions
1.Test out different slang on the Naive Bayes Classifier! What happens when you use the word “lit” to mean “wonderful” or “fun”?

Is the sentiment prediction accurate? Test out different slang.


```python
from reviews import counter, training_counts
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Add your review:
review = "It was lit!"
review_counts = counter.transform([review])

classifier = MultinomialNB()
training_labels = [0] * 1000 + [1] * 1000

classifier.fit(training_counts, training_labels)

neg = (classifier.predict_proba(review_counts)[0][0] * 100).round()
pos = (classifier.predict_proba(review_counts)[0][1] * 100).round()

if pos > 50:
  print("Naive Bayes classifies this as positive.")
elif neg > 50:
  print("Naive Bayes classifies this as negative.")
else:
  print("Naive Bayes cannot determine if this is negative or positive.")
  

print("\nAccording to our trained Naive Bayes classifier, 
the probability that your review was negative was {0}% and the probability it was positive was {1}%.".format(neg, pos))
