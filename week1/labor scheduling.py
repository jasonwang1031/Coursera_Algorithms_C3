def jobschedule(joblist):
    jobs = sorted(joblist,key = lambda x:(x[2],x[0]))
    jobs = jobs[-1::-1]
    sumTime = 0
    sumLength = 0 
    for job in jobs:
        sumLength += job[1]
        sumTime += job[0] * sumLength
    print(sumTime)


if __name__ == "__main__":
    f = open('quiz1.txt','r')
    lines = f.readlines()[1:]
    jobs = []

    for line in lines:
        weight = int(line.split()[0])
        length = int(line.split()[1])
        jobs.append([weight,length,weight - length])
    jobschedule(jobs)