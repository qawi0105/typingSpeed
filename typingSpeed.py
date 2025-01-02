import time

print("Welcome to the Typing Speed Test!")
print("Type the following sentence as fast as you can:\n")

sentence = "The quick brown fox jumps over the lazy dog."
print(f"👉 {sentence}")
input("\nPress Enter when you're ready to start...")

# Start the timer
start_time = time.time()

# User types the sentence
typed_sentence = input("\nType the sentence: ")

# End the timer
end_time = time.time()

# Calculate time taken and check accuracy
time_taken = end_time - start_time
accuracy = sum(1 for a, b in zip(sentence, typed_sentence) if a == b) / len(sentence) * 100

print(f"\nTime taken: {time_taken:.2f} seconds")
print(f"Accuracy: {accuracy:.2f}%")

if accuracy == 100:
    print("🎉 Perfect typing! You're amazing!")
elif accuracy >= 80:
    print("👍 Great job! Keep practicing!")
else:
    print("💪 Don't worry, keep practicing to improve!")
