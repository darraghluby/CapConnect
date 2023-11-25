from Hello import st
from Hello import Image

st.set_page_config(page_title="Introduction to patient guidance and information")
image = Image.open("images/cc.png")

st.image(image)

text = """
# Overview of Cold Cap Treatment

Provide a concise yet thorough explanation of what cold cap treatment involves, including the purpose, benefits, and potential challenges.

## Treatment Process

Outline the step-by-step procedure of using the cold cap, from preparation to post-treatment care. This includes how to wear the cap, the duration of each session, and any specific guidelines to follow.

## Expected Sensations

Describe what sensations patients might experience during the treatment, such as coldness or tightness, to manage expectations and reduce anxiety.

## Hair Care Guidelines

Offer detailed guidance on how to care for the hair before, during, and after treatment. This may include recommendations for gentle hair care products and practices.

## Potential Side Effects

Clearly communicate potential side effects and their likelihood. This includes temporary discomfort, changes in hair texture, and, importantly, the possibility of hair shedding.

## Effectiveness and Success Rates

Share information on the efficacy of cold cap treatment, providing realistic expectations and success rates. This can help patients make informed decisions about their treatment journey.

## Preparation Tips

Offer practical advice on how to prepare for each treatment session, covering aspects like clothing choices, hydration, and any recommended pre-treatment rituals.

## Duration and Frequency

Clearly outline the recommended duration and frequency of cold cap sessions, ensuring patients understand the commitment involved.

## Possible Adjustments

Explain if and how the treatment plan might be adjusted based on individual responses or changing conditions.

## Contact Information and Support

Provide easily accessible contact information for medical professionals and support staff, emphasizing that patients can reach out with any questions or concerns.

## Interactive Features

Include interactive elements such as FAQs, video tutorials, and virtual tours to enhance understanding and engagement.

## Tracking and Progress

Incorporate features for patients to track their treatment progress, offering a sense of control and motivation.
"""

st.markdown(text)