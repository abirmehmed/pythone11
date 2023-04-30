import random

# Open the file containing Chinese pinyin and meaning
with open('chinese_vocab.txt', 'r') as f:
    lines = f.readlines()

vocab = {}
for line in lines:
    pinyin, meaning, char = line.strip().split('\t')
    vocab[char] = (pinyin, meaning)

# Set up the quiz
num_correct = 0
num_total = 10
for i in range(num_total):
    # Choose a random character from the vocab
    char = random.choice(list(vocab.keys()))

    # Get the correct pinyin and meaning for the character
    correct_pinyin, correct_meaning = vocab[char]

    # Choose three random incorrect pinyin options
    all_pinyin_options = [correct_pinyin]
    while len(all_pinyin_options) < 4:
        random_char = random.choice(list(vocab.keys()))
        if random_char != char:
            all_pinyin_options.append(vocab[random_char][0])
    random.shuffle(all_pinyin_options)

    # Print the question and answer options
    print('Question', i+1)
    print('What is the meaning of this character:', char)
    for j in range(4):
        print(str(j+1) + '.', all_pinyin_options[j])
    user_choice = input('Enter your answer (1-4): ')

    # Check if the user's answer is correct and print the result
    if user_choice == '1' and all_pinyin_options[0] == correct_pinyin:
        print('Correct!')
        num_correct += 1
    elif user_choice == '2' and all_pinyin_options[1] == correct_pinyin:
        print('Correct!')
        num_correct += 1
    elif user_choice == '3' and all_pinyin_options[2] == correct_pinyin:
        print('Correct!')
        num_correct += 1
    elif user_choice == '4' and all_pinyin_options[3] == correct_pinyin:
        print('Correct!')
        num_correct += 1
    else:
        print('Incorrect. The correct answer was:', correct_pinyin)

# Print the final score
print('You got', num_correct, 'out of', num_total, 'questions correct.')
