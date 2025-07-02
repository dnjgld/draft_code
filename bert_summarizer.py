# Bert Summarization
from summarizer import Summarizer

input_text = """

Once upon a time there lived in a certain village a little country girl, the prettiest creature who was ever seen. Her mother was excessively fond of her; and her grandmother doted on her still more. This good woman had a little red riding hood made for her. It suited the girl so extremely well that everybody called her Little Red Riding Hood.

One day her mother, having made some cakes, said to her, "Go, my dear, and see how your grandmother is doing, for I hear she has been very ill. Take her a cake, and this little pot of butter."

Little Red Riding Hood set out immediately to go to her grandmother, who lived in another village.

As she was going through the wood, she met with a wolf, who had a very great mind to eat her up, but he dared not, because of some woodcutters working nearby in the forest. He asked her where she was going. The poor child, who did not know that it was dangerous to stay and talk to a wolf, said to him, "I am going to see my grandmother and carry her a cake and a little pot of butter from my mother."

"Does she live far off?" said the wolf

"Oh I say," answered Little Red Riding Hood; "it is beyond that mill you see there, at the first house in the village."

"Well," said the wolf, "and I'll go and see her too. I'll go this way and go you that, and we shall see who will be there first."

"""

summarizer = Summarizer()

summary = summarizer(input_text, min_length=50, max_length=150)

print("Original Text:\n" + input_text)

print("\nSummary:\n"+summary)

# BART Abstractive Summarization

# Google’s T5 Abstractive Summarization

# Gensim (Extractive Summarization)

# SUMY (extractive summarization)

# Pysummarization