import datetime



Mood={'happy':2,
        'relaxed':1,
        'apathetic':0,
        'sad':-1,
        'angry':-2}

def once():
    date_today = datetime.date.today() # get the date today as a date object
    date_today = str(date_today)
    with open('data/mood_diary.txt','r') as f:
        for line in f.readlines():
            if line.startswith(date_today):
                return True
    return False

def mood():
    while True:
        mood = input('Enter your current mood: `happy`, `relaxed`, `apathetic`, `sad`, or `angry`')
        if mood in ['happy','relaxed','apathetic','sad','angry']:
            date_today=datetime.date.today()
            with open('data/mood_diary.txt',"a") as f:
                f=f.write(f'{date_today},{Mood[mood]}\n')
            return Mood[mood]


        
def once_2():
     if once():
        print('Sorry, you have already entered your mood today.')
        return
     else:
        mood()

def assess_mood():
    once_2()
    Mood={2:'happy',
         1:'relaxed',
         0:'apathetic',
         -1:'sad',
         -2:'angry'}

    entries=[]
    f=open('data/mood_diary.txt','r')
    entries=f.readlines()
    f.close()

    if len(entries)<7:
        return
    
    entries_7=entries[-7:]
    mood_for_7=0
    for entry in entries_7:
        mood_sum_2=int(entry.split(',')[1])
        mood_for_7+=mood_sum_2
    print(f'{mood_for_7}')
    print(mood_sum_2)
    
    average = round(mood_for_7/7)
    mood_account = {2:0, 1:0, 0:0, -1:0, -2:0}
    for line in entries_7:
        mood_=int(line.split(',')[1])
        mood_account[mood_]+=1
    if mood_account[2]>=5:
        diagnosis='manic'
    elif mood_account[-1]>=4:
        diagnosis='depressive'
    elif mood_account[0]>=6:
        diagnosis='schizoid'
    else:
        diagnosis=Mood[average]
        # diagnosis = [mood for mood, value in Mood.items() if value == average][0]
    print(f'(Your diagnosis:{diagnosis})')


    