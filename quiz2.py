
def jobschedule(joblist):
    jobs = sorted(joblist,key = lambda job:(job[0],job[1]))
    # sorting first by ratio than by weight
    jobs.reverse()
    TotalLength = 0
    WeightedTime = 0 
    for job in jobs:
        TotalLength += job[2]
        WeightedTime += job[1] * TotalLength
    print(WeightedTime)


if __name__ == "__main__":
    f = open('quiz1.txt','r')
    lines = f.readlines()[1:]
    jobs = []

    for line in lines:
        weight = int(line.split()[0])
        length = int(line.split()[1])
        jobs.append([weight/length,weight,length])
    jobschedule(jobs)