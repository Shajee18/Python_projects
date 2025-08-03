import random
import time

Questions = [
                    
    { 
      "question" : "Which one of the following is a base quantity?",
      "options"   : ["A) Speed","B) Force","C) Mass","D) Area"],
      "answer" : "C"
    },
  
    {
        "question": "The correct unit of density in SI system is:",
        "options": ["A) kg/m²","B) kg/m³","C) g/cm³","D) N/m³"],
        "answer":"B"
     


    },
    {
        "question":"3. The slope of a distance-time graph gives:",
        "options": ["A) Velocity","B) Acceleration","C) Displacement","D) Force"],
        "answer":"A"

    },
    {
        "question":"A body is moving with uniform velocity, then its acceleration is:",
        "options": ["A) Positive","B) Zero","C) Negative","D) Constant"],
        "answer": "B"
    
    },
    {
        "question": "The inertia of a body depends on its:",
        "options": ["A) Volume","B) Speed","C) Mass","D) Shape"],
        "answer":"C"
    },
    {
        "question": "Action and reaction forces act:",
        "options": ["A) On the same body","B) On different bodies","C) In the same direction","D) At different times"],
        "answer": "B"
        
    },
    {
        "question":"The unit of moment of force is:",
        "options":["A) N","B) Nm","C) N/m","D) kgm/s²"],
        "answer":"B"
    },
    {
        "question":" A body is in equilibrium if:",
        "options":["A) Only one force acts on it","B) Net force is zero","C) Net torque is zero","D) Both B and C"],
        "answer":"D"
    },
    {
        "question":"The value of 'g' on the Moon is:",
        "options":["A) Same as Earth","B) Greater than Earth","C) Less than Earth","D) Zero"],
        "answer":"C"
    },
    {
        "question": "Weight of a body is:",
        "options":["A) Constant everywhere","B) Same as mass","C) A vector quantity","D) A scalar quantity"],
        "answer":"C"
    },
]
num_Questions = 5
selected_questions = random.sample(Questions,num_Questions)
start_time = time.time()


score = 0
print("\n==== Quiz Started ====\n")

for i, q in enumerate(selected_questions,1):
    print(f"Q{i} : {q['question']}")
    for options in q['options']:
        print(options)
    answer = input("your answer (a/b/c/d):").strip().upper()
    if answer == q['answer'].strip().upper():
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer is: {q['answer']})\n")

end_time = time.time()
total_time = round(end_time-start_time,2)


print("==== Quiz Ended ====")
print(f"Your Score: {score} out of {num_Questions}")
print(f"Time Taken: {total_time} seconds")

