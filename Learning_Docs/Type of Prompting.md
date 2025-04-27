# Single-Shot, Multi-Shot, and Zero-Shot Prompting Explained

These terms describe different ways of instructing AI models by providing examples (or not) before asking them to perform a task.

## Zero-Shot Prompting

This is when you ask an AI to perform a task without showing it any examples first.

**Example:**
```
Classify this movie review as positive or negative:
"The acting was terrible and the plot made no sense. Complete waste of time."
```

Here, you're directly asking the AI to classify the sentiment without showing it how to do it first.

## One-Shot/Single-Shot Prompting

This is when you provide exactly one example of the task before asking the AI to perform a similar task.

**Example:**
```
Movie review: "The special effects were amazing and the story kept me engaged throughout."
Classification: Positive

Movie review: "The acting was terrible and the plot made no sense. Complete waste of time."
Classification:
```

You've shown one example of how to classify a positive review before asking for the new classification.

## Few-Shot/Multi-Shot Prompting

This is when you provide multiple examples before asking the AI to perform the task.

**Example:**
```
Movie review: "The special effects were amazing and the story kept me engaged throughout."
Classification: Positive

Movie review: "I fell asleep halfway through and couldn't bring myself to finish it."
Classification: Negative

Movie review: "While the cinematography was beautiful, the characters were flat and uninteresting."
Classification: Mixed

Movie review: "The acting was terrible and the plot made no sense. Complete waste of time."
Classification:
```

By showing multiple examples with varying classifications, you're helping the AI understand the pattern and nuances of the task.

## Why This Matters

- **Zero-shot** is convenient but may be less accurate for complex or nuanced tasks
- **Single-shot** helps establish the format and basic understanding
- **Multi-shot** usually leads to better performance as the AI can recognize patterns from multiple examples

The more complex or specialized the task, the more examples can help guide the AI to produce the results you want.