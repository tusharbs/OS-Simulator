# coding=utf-8
from tkinter import *

from tkinter.font import *
from PIL import Image, ImageTk
import tkinter.simpledialog as tkSimpleDialog
import tkinter.messagebox as messagebox


import time
import math
procMax=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


class process:
    pno = 0
    at = 0
    ct = 0
    bt = 5
    wt = 0
    tat = 0
    flag = -1
    tbt = 0
    pri = 0


timer = 0
avgtat = 0
avgwt = 0
prolist = []
for i in range(0, 10):
    prolist.append(process())


def read_process(procNo):
    global procMax
    global prolist
    for i in range(0, procNo):
        prolist[i].at = procMax[i][0]
        prolist[i].bt = procMax[i][1]
        prolist[i].pri = procMax[i][2]
        prolist[i].pno = i
        prolist[i].tbt = prolist[i].bt


def sjf():
    global avgwt
    global avgtat
    global procNo
    global prolist
    global mini
    global timer
    global frame1
    label7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ctr = 0
    frame1.destroy()
    frame1 = Frame(window)
    frame1.pack(side=TOP, pady=0)
    label8 = Label(window, bg='green', text=str(ctr))
    label8.place(x=5, y=5)
    label15 = Label(window, bg='white', height=4, width=100, anchor=S, text="                             Process             State ", )
    label15.place(x=150, y=0)
    for i in range(0, procNo):
        label[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label7[i] = Label(label[i], bg='grey', width=10, height=2, text="Not arrived")
        label[i].grid(row=2 * i, column=100)
        label7[i].grid()
    for i in range(0, procNo):
        label12[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label13[i] = Label(label12[i], bg='red', width=10, height=2, text="Process" + str(i+1))
        label12[i].grid(row=2 * i, column=0)
        label13[i].grid()
    label16 = Label(window, bg='light blue', height=9, width=150, anchor=W, text="Shortest job next (SJN), also known as shortest job first (SJF) or shortest process next (SPN), is a scheduling policy that selects for execution the waiting process with the smallest execution\ntime. SJN is a non-pre-emptive algorithm. Shortest remaining time is a pre-emptive variant of SJN. Shortest job next is advantageous because of its simplicity and because it minimizes the \naverage amount of time each process has to wait until its execution is complete. However, it has the potential for process starvation for processes which will require a long time to complete if \nshort processes are continually added. Highest response ratio next is similar but provides a solution to this problem using a technique called aging. Another disadvantage of using shortest job \nnext is that the total execution time of a job must be known before execution. While it is impossible to predict execution time perfectly, several methods can be used to estimate it, such as a \nweighted average of previous execution times. Shortest job next can be effectively used with interactive processes which generally follow a pattern of alternating between waiting for a \ncommand and executing it. If the execution burst of a process is regarded as a separate job, past behaviour can indicate which process to run next, based on an estimate of its running time.\nShortest job next is used in specialized environments where accurate estimates of running time are available.\n",)
    label16.place(x=20, y=450)

    read_process(procNo)
    for i in range(0, procNo):
        for j in range(0, procNo - i - 1):
            if prolist[j].at > prolist[j + 1].at:
                prolist[j], prolist[j + 1] = prolist[j + 1], prolist[j]

    timer = 0
    timer = timer + prolist[0].at
    for j in range(0, prolist[0].at):
        label8.config(text=str(ctr))
        ctr = ctr + 1
        for e in range(0, procNo):
            if (prolist[e].at <= ctr):
                label7[e].config(bg="grey", text="not arrived")
        window.update()
        time.sleep(1)
    for j in range(0, procNo):
        min = 1000
        max2 = 1000
        for i in range(0, procNo):
            if prolist[i].bt < min and prolist[i].at <= timer and prolist[i].flag == -1:
                min = prolist[i].bt
                mini = i
        if min == 1000:
            x = mini
            for i in range(0, procNo):
                if prolist[i].at <= max2 and prolist[i].flag == -1:
                    max2 = prolist[i].at
                    mini = i
                    z = prolist[mini].at - prolist[x].ct
                    timer = timer + prolist[mini].at - prolist[x].ct
                    for i in range(0, z):
                        label8.config(text=str(ctr))
                        ctr = ctr + 1
                        window.update()
                        time.sleep(1)

        timer = timer + prolist[mini].bt
        prolist[mini].ct = timer
        prolist[mini].tat = prolist[mini].ct - prolist[mini].at
        prolist[mini].wt = prolist[mini].tat - prolist[mini].bt
        prolist[mini].flag = 0
        avgtat = avgtat + prolist[mini].tat
        avgwt = avgwt + prolist[i].tat
        for k in range(0, prolist[mini].bt):
            label7[mini].config(bg="blue", text="Running")
            ctr += 1
            for e in range(0, procNo):
                if (prolist[e].at <= ctr and prolist[e].flag == -1):
                    label7[e].config(bg="yellow", text="in queue")
                    window.update()
            label8.config(text=str(ctr))
            window.update()
            time.sleep(1)
        label7[mini].config(bg="green", text="Done")
        messagebox.showinfo("Process-" + str(mini+1) + " completed",
                            " completion time=" + str(timer) + "\nturn around time=" + str(
                                prolist[mini].tat) + "\nwaiting time=" + str(prolist[mini].wt))
    avgtat = avgtat / procNo
    avgwt = avgwt / procNo
    for i in range(0, procNo):
        print(prolist[i].at, prolist[i].bt, prolist[i].ct, prolist[i].tat, prolist[i].wt)


# Round Robin
def empty():
    global f
    if f == -1:
        return 0
    else:
        return 1


f = -1
r = -1
q = []
for i in range(0, 50):
    q.append(process())

p = process()


def enque(p):
    global f
    global r
    if f == -1:
        f = f + 1
        r = r + 1
    else:
        r = r + 1
    q[r] = p


def deque():
    global f
    global r
    o = process()
    o = q[f]
    if f == r:
        f = -1
        r = -1
    else:
        f = f + 1
    return o


tq = 0


def rr():
    global avgwt
    global avgtat
    global procNo
    global prolist
    global timer
    global tq
    global frame1
    print("hello")
    label7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ctr = 0
    frame1.destroy()
    frame1 = Frame(window)
    frame1.pack(side=TOP, pady=0)
    label8 = Label(window, bg='green', text=str(ctr))
    label8.place(x=5, y=5)
    label15 = Label(window, bg='white', height=4, width=100, anchor=S, text="                             Process             State ", )
    label15.place(x=150, y=0)
    for i in range(0, procNo):
        label[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label7[i] = Label(label[i], bg='grey', width=10, height=2, text="Not arrived")
        label[i].grid(row=2 * i, column=100)
        label7[i].grid()
    for i in range(0, procNo):
        label12[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label13[i] = Label(label12[i], bg='red', width=10, height=2, text="Process" + str(i+1))
        label12[i].grid(row=2 * i, column=0)
        label13[i].grid()
        label16 = Label(window, bg='light blue', height=9, width=150, anchor=W, text="Round-robin (RR) is one of the algorithms employed by process and network schedulers in computing.As the term is generally used, time slices (also known as time quanta) are assigned to each  \nprocess in equal portions and in circular order, handling all processes without priority (also known as cyclic executive). Round-robin scheduling is simple, easy to implement,and starvation-free.\nRound-robin scheduling can also be applied to other scheduling problems, such as data packet scheduling in computer networks. It is an operating system concept. The name of the algorithm\ncomes from the round-robin principle known from other fields, where each person takes an equal share of something in turn. To schedule processes fairly, a round-robin scheduler generally\nemploys time-sharing, giving each job a time slot or quantum (its allowance of CPU time), and interrupting the job if it is not completed by then. The job is resumed next time a time slot is\nassigned to that process. If the process terminates or changes its state to waiting during its attributed time quantum, the scheduler selects the first process in the ready queue to execute. In the\nabsence of time-sharing, or if the quanta were large relative to the sizes of the jobs, a process that produced large jobs would be favoured over other processes. Round-robin algorithm is a\npre-emptive algorithm as the scheduler forces the process out of the CPU once the time quota expires.",)
    label16.place(x=18, y=450)

    x = process()
    tq = tkSimpleDialog.askinteger("tq", "Enter time quannta")

    read_process(procNo)
    timer=0
    for i in range(0, procNo):
        for j in range(0, procNo - i - 1):
            if prolist[j].at > prolist[j + 1].at:
                prolist[j], prolist[j + 1] = prolist[j + 1], prolist[j]


    for j in range(0, prolist[0].at):
        label8.config(text=str(ctr))
        ctr = ctr + 1   
        window.update()
        time.sleep(1)
    timer=timer+prolist[0].at
    enque(prolist[0])

    prev = 0
    while empty() != 0:
        prev = timer
        x = deque()
        if x.tbt <= int(tq) and x.flag == -1:
            timer = timer + x.tbt
            for j in range(0, x.tbt):
                ctr += 1
                label8.config(text=str(ctr))

                for e in range(0, procNo):
                    if prolist[e].flag == -1:
                        if e == x.pno:
                            label7[e].config(bg="blue", text="running")
                        if (prolist[e].at <= ctr and prolist[e].flag == -1 and e != x.pno):
                            label7[e].config(bg="yellow", text="in queue")
                        if (prolist[e].at > ctr and prolist[e].flag == -1 and e != x.pno):
                            label7[e].config(bg="grey", text="not arrived")
                window.update()
                time.sleep(1)

            x.tbt = 0
            x.ct = timer
            x.tat = x.ct - x.at
            x.wt = x.tat - x.bt
            x.flag = 0
            label7[x.pno].config(bg="green", text="Done")
            messagebox.showinfo("Process-" + str(x.pno+1) + " completed",
                                " completion time=" + str(timer) + "\nturn around time=" + str(
                                    prolist[x.pno].tat) + "\nwaiting time=" + str(prolist[x.pno].wt))
            window.update()
        else:
            x.tbt = x.tbt - int(tq)
            timer = timer + int(tq)
            for e in range(0, int(tq)):
                ctr += 1
                label8.config(text=str(ctr))
                for e in range(0, procNo):
                    if prolist[e].flag == -1:
                        if e == x.pno:
                            label7[e].config(bg="blue", text="running")
                        if (prolist[e].at <= ctr and prolist[e].flag == -1 and e != x.pno):
                            label7[e].config(bg="yellow", text="in queue")
                        if (prolist[e].at > ctr and prolist[e].flag == -1 and e != x.pno):
                            label7[e].config(bg="grey", text="not arrived")
                window.update()
                time.sleep(1)

        for i in range(0, procNo):
            if prolist[i].at >= prev and prolist[i].at <= timer and prolist[i].pno!=x.pno and prolist[i].wt!=-1:
                prolist[i].wt=-1
                enque(prolist[i])
        if x.flag == -1:
            enque(x)

    for i in range(0, procNo):
        print(prolist[i].at, prolist[i].bt, prolist[i].ct)

# Preemptive priority

def pp():
    global avgwt
    global avgtat
    global procNo
    global prolist
    global timer
    global tq
    global frame1

    label7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ctr = 0
    frame1.destroy()
    frame1 = Frame(window)
    frame1.pack(side=TOP, pady=0)
    label8 = Label(window, bg='green', text=str(ctr))
    label8.place(x=5, y=5)
    label15 = Label(window, bg='white', height=3, width=100, anchor=S, text="                             Process             State ", )
    label15.place(x=150, y=0)
    for i in range(0, procNo):
        label[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label7[i] = Label(label[i], bg='grey', width=10, height=2, text="Not arrived")
        label[i].grid(row=2 * i, column=100)
        label7[i].grid()
    for i in range(0, procNo):
        label12[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label13[i] = Label(label12[i], bg='red', width=10, height=2, text="Process" + str(i+1))
        label12[i].grid(row=2 * i, column=0)
        label13[i].grid()
    label16 = Label(window, bg='light blue', height=9, width=150, anchor=N, text="The operating system assigns a fixed priority rank to every process, and the scheduler arranges the processes in the ready queue in order of their priority. Lower-priority processes get\ninterrupted by incoming higher-priority processes.\n.1.Overhead is not minimal, nor is it significant.\n.2.FPPS has no particular advantage in terms of throughput over FIFO scheduling.\n.3.If the number of rankings is limited, it can be characterized as a collection of FIFO queues, one for each priority ranking. Processes in lower-priority queues are selected only when all of the\nhigher-priority queues are empty.\n.4.Waiting time and response time depend on the priority of the process. Higher-priority processes have smaller waiting and response times.\n.5.Deadlines can be met by giving processes with deadlines a higher priority.\n.6.Starvation of lower-priority processes is possible with large numbers of high-priority processes queuing for CPU time.\n",)
    label16.place(x=18, y=450)

    read_process(procNo)

    for i in range(0, procNo):
        for j in range(0, procNo - i - 1):
            if prolist[j].at > prolist[j + 1].at:
                prolist[j], prolist[j + 1] = prolist[j + 1], prolist[j]
    timer = 0
    timer = timer + prolist[0].at
    for j in range(0, prolist[0].at):
        label8.config(text=str(ctr))
        for e in range(0,procNo):
            if prolist[e].at<=ctr:
                label7[e].config(bg="yellow", text="in queue")
        ctr = ctr + 1
        window.update()
        time.sleep(1)

    s = 0
    avgtat = 0.0
    avgwt = 0.0
    while (s == 0):
        #maxy = 0
        max1 = -1
        max2 = 100
        for i in range(0, procNo):
            if prolist[i].pri >= max1 and prolist[i].flag == -1 and prolist[i].at <= timer:
                max1 = prolist[i].pri
                maxy = i
        if prolist[maxy].tbt == 0:
            prolist[maxy].ct = timer
            prolist[maxy].flag = 0
            prolist[maxy].tat = prolist[maxy].ct - prolist[maxy].at
            prolist[maxy].wt = prolist[maxy].tat - prolist[maxy].bt
            avgtat = avgtat + prolist[maxy].tat
            avgwt = avgwt + prolist[maxy].wt
            label7[prolist[maxy].pno].config(bg="green", text="Done")
            messagebox.showinfo("Process-" + str(prolist[maxy].pno+1) + " completed",
                                " completion time=" + str(prolist[maxy].ct) + "\nturn around time=" + str(
                                    prolist[maxy].tat) + "\nwaiting time=" + str(prolist[maxy].wt))

            window.update()

        if max1 == -1:
            x = maxy
            for i in range(0, procNo):
                if prolist[i].at <= max2 and prolist[i].flag == -1:
                    max2 = prolist[i].at
                    maxy = i
            timer = timer + prolist[maxy].at - prolist[x].ct
        prolist[maxy].tbt = prolist[maxy].tbt - 1
        timer = timer + 1
        ctr += 1

        label8.config(text=str(ctr))
        if prolist[maxy].tbt == 0:
            prolist[maxy].ct = timer
            prolist[maxy].flag = 0
            prolist[maxy].tat = prolist[maxy].ct - prolist[maxy].at
            prolist[maxy].wt = prolist[maxy].tat - prolist[maxy].bt
            avgtat = avgtat + prolist[maxy].tat
            avgwt = avgwt + prolist[maxy].wt
            label7[prolist[maxy].pno].config(bg="green", text="Done")
            messagebox.showinfo("Process-" + str(prolist[maxy].pno+1) + " completed",
                                " completion time=" + str(prolist[maxy].ct) + "\nturn around time=" + str(
                                    prolist[maxy].tat) + "\nwaiting time=" + str(prolist[maxy].wt))
            window.update()


        for e in range(0, procNo):
            if prolist[e].flag == -1:
                if e == maxy:
                    label7[prolist[e].pno].config(bg="blue", text="running")
                if (prolist[e].at <= timer and prolist[e].flag == -1 and e != maxy):
                    label7[prolist[e].pno].config(bg="yellow", text="in queue")
                if (prolist[e].at > timer and prolist[e].flag == -1 and e != maxy):
                    label7[prolist[e].pno].config(bg="grey", text="not arrived")

        window.update()
        time.sleep(1)



        q1 = 0

        for k in range(0, procNo):
            if prolist[k].flag == 0:
                q1 = q1 + 1
        if q1 == procNo:
            s = 1
            break

#srtf
def srtf():
    global avgwt
    global avgtat
    global procNo
    global prolist
    global timer
    global tq
    global frame1

    label7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ctr = 0
    timer=0
    frame1.destroy()
    frame1 = Frame(window)
    frame1.pack(side=TOP, pady=0)
    label8 = Label(window, bg='green', text=str(ctr))
    label8.place(x=5, y=5)
    label15 = Label(window, bg='white', height=4, width=100, anchor=S, text="                             Process             State ", )
    label15.place(x=150, y=0)
    for i in range(0, procNo):
        label[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label7[i] = Label(label[i], bg='grey', width=10, height=2, text="Not arrived")
        label[i].grid(row=2 * i, column=100)
        label7[i].grid()
    for i in range(0, procNo):
        label12[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label13[i] = Label(label12[i], bg='red', width=10, height=2, text="Process" + str(i+1))
        label12[i].grid(row=2 * i, column=0)
        label13[i].grid()
    label16 = Label(window, bg='light blue', height=9, width=150, anchor=N, text="Shortest remaining time, also known as shortest remaining time first (SRTF), is a scheduling method that is a pre-emptive version of shortest job next scheduling.\nIn this scheduling algorithm, the process with the smallest amount of time remaining until completion is selected to execute. Since the currently executing process is the one with the\nshortest amount of time remaining by definition, and since that time should only reduce as execution progresses, processes will always run until they complete or a new process is added\nthat requires a smaller amount of time. Shortest remaining time is advantageous because short processes are handled very quickly. The system also requires very little overhead since it\nonly makes a decision when a process completes or a new process is added, and when a new process is added the algorithm only needs to compare the currently executing process with the\nnew process, ignoring all other processes currently waiting to execute. Like shortest job first, it has the potential for process starvation; long processes may be held off indefinitely\nif short processes are continually added. This threat can be minimal when process times follow a heavy-tailed distribution. A similar algorithm which avoids starvation at the cost of\nhigher tracking overhead is highest response ratio next. Like shortest job next scheduling, shortest remaining time scheduling is rarely used outside of specialized environments because\nit requires accurate estimates of the runtime of each process.\n",)
    label16.place(x=18, y=450)
    remain=0
    read_process(procNo)
    prolist[9].tbt = 9999
    while remain != procNo:
        smallest = 9
        for i in range(0,procNo):
            if prolist[i].at <= timer and prolist[i].tbt < prolist[smallest].tbt and prolist[i].tbt > 0:
                smallest = i
        prolist[smallest].tbt = prolist[smallest].tbt - 1
        if smallest!=9:
            for e in range(0,procNo):
                if prolist[e].flag == -1:
                    if e == smallest:
                        label7[e].config(bg="blue", text="running")
                    if (prolist[e].at <= ctr and prolist[e].flag == -1 and e != smallest):
                        label7[e].config(bg="yellow", text="in queue")
                    if (prolist[e].at > ctr and prolist[e].flag == -1 and e != smallest):
                        label7[e].config(bg="grey", text="not arrived")

        if prolist[smallest].tbt == 0:
            remain += 1
            endtime = timer + 1
            ctr=endtime
            label8.config(text=str(ctr))
            window.update()
            prolist[smallest].tat = endtime - prolist[smallest].at
            prolist[smallest].wt = endtime - prolist[smallest].bt - prolist[smallest].at
            prolist[smallest].ct = endtime
            prolist[smallest].flag=0
            label7[smallest].config(bg="green", text="Done")
            messagebox.showinfo("Process-" + str(smallest+1) + " completed"," completion time=" + str(endtime) + "\nturn around time=" + str(prolist[smallest].tat) + "\nwaiting time=" + str(prolist[smallest].wt))
            # print smallest+1,'\t',prolist[smallest].at,'\t',prolist[smallest].bt,'\t',endtime-prolist[smallest].at,'\t',endtime-prolist[smallest].bt-prolist[smallest].at,'\n'
            avgwt += endtime - prolist[smallest].bt - prolist[smallest].at
            avgtat += endtime - prolist[smallest].at
        timer = timer + 1
        ctr=ctr+1
        label8.config(text=str(ctr))
        window.update()
        time.sleep(1)


# fcfs
def fcfs():
    global avgwt
    global avgtat
    global procNo
    global prolist
    global timer
    global tq
    global frame1

    label7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    label13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ctr = 0
    frame1.destroy()
    frame1 = Frame(window)
    frame1.pack(side=TOP, pady=0)
    label8 = Label(window, bg='green', text=str(ctr))
    label8.place(x=5, y=5)
    label15 = Label(window, bg='white', height=4, width=100, anchor=S, text="                             Process             State ", )
    label15.place(x=150, y=0)
    for i in range(0, procNo):
        label[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label7[i] = Label(label[i], bg='grey', width=10, height=2, text="Not arrived")
        label[i].grid(row=2 * i, column=100)
        label7[i].grid()
    for i in range(0, procNo):
        label12[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label13[i] = Label(label12[i], bg='red', width=10, height=2, text="Process" + str(i+1))
        label12[i].grid(row=2 * i, column=0)
        label13[i].grid()
    label16 = Label(window, bg='light blue', height=11, width=150, anchor=N, text="First in, first out, also known as first come, first served (FCFS), is the simplest scheduling algorithm. FIFO simply queues processes in the order that they arrive in the ready queue.\nThis is commonly used for a task queue, for example as illustrated in this section.\n.1.Since context switches only occur upon process termination, and no reorganization of the process queue is required, scheduling overhead is minimal.\n.2.Throughput can be low, because long processes can be holding CPU, waiting the short processes for a long time (known as convoy effect).\n.3.No starvation, because each process gets chance to be executed after a definite time.\n.4.Turnaround time, waiting time and response time depends on the order of their arrival and can be high for the same reasons above.\n.5.No prioritization occurs, thus this system has trouble meeting process deadlines.\n.6.The lack of prioritization means that as long as every process eventually completes, there is no starvation. In an environment where some processes might not complete, there\ncan be starvation.\n.7.It is based on queuing.",)
    label16.place(x=18, y=450)

    read_process(procNo)
    for i in range(0, procNo):
        for j in range(0, procNo - i - 1):
            if prolist[j].at > prolist[j + 1].at:
                prolist[j], prolist[j + 1] = prolist[j + 1], prolist[j]

    timer = 0
    timer = timer + prolist[0].at
    for j in range(0, prolist[0].at):
        label8.config(text=str(ctr))
        ctr = ctr + 1
        for e in range(0, procNo):
            if (prolist[e].at <= ctr):
                label7[e].config(bg="yellow", text="in queue")
                window.update()
        label8.config(text=str(ctr))
        window.update()
        time.sleep(1)

    timer = timer + prolist[0].bt

    prolist[0].ct = prolist[0].at + prolist[0].bt
    prolist[0].tat = prolist[0].ct - prolist[0].at
    prolist[0].wt = prolist[0].tat - prolist[0].bt

    for k in range(0, prolist[0].bt):
        label7[0].config(bg="blue", text="Running")
        ctr += 1
        window.update()
        for e in range(0, procNo):
            if (prolist[e].at <= ctr and prolist[e].flag == -1 and e!=0):
                label7[e].config(bg="yellow", text="in queue")
                window.update()
        label8.config(text=str(ctr))
        window.update()
        time.sleep(1)
    prolist[0].flag=0
    label7[0].config(bg="green", text="Done")
    messagebox.showinfo("Process-" + str(0+1) + " completed", " completion time=" + str(timer) + "\nturn around time=" + str(
        prolist[0].tat) + "\nwaiting time=" + str(prolist[0].wt))

    for i in range(1, procNo):
        if prolist[i].at<=timer:
            timer = timer + prolist[i].bt
            prolist[i].ct = prolist[i - 1].ct + prolist[i].bt
            prolist[i].tat = prolist[i].ct - prolist[i].at
            prolist[i].wt = prolist[i].tat - prolist[i].bt
        else:
            for h in range(0, prolist[i].at-prolist[i-1].ct):
                ctr = ctr + 1
                label8.config(text=str(ctr))
                window.update()
                time.sleep(1)
            timer = prolist[i].at + prolist[i].bt
            prolist[i].ct = prolist[i].at + prolist[i].bt
            prolist[i].tat = prolist[i].ct - prolist[i].at
            prolist[i].wt = prolist[i].tat - prolist[i].bt              

        avgtat += prolist[i].tat
        avgwt += prolist[i].wt
        for k in range(0, prolist[i].bt):
            label7[i].config(bg="blue", text="Running")
            ctr += 1
            window.update()
            for e in range(0, procNo):
                if (prolist[e].at <= ctr and prolist[e].flag == -1 and e!=i):
                    label7[e].config(bg="yellow", text="in queue")
                    window.update()
            label8.config(text=str(ctr))
            window.update()
            time.sleep(1)
        label7[i].config(bg="green", text="Done")
        messagebox.showinfo("Process-" + str(i+1) + " completed",
                            " completion time=" + str(timer) + "\nturn around time=" + str(
                                prolist[i].tat) + "\nwaiting time=" + str(prolist[i].wt))
        prolist[i].flag=0
    avgtat /= procNo
    avgwt /= procNo

    for i in range(0, procNo):
        print(prolist[i].at, prolist[i].bt, prolist[i].ct, prolist[i].tat, prolist[i].wt)


#Non preemptive priority
def nonpri():
    global avgwt
    global avgtat
    global procNo
    global prolist
    global timer
    global tq
    global frame1

    label7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    label13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    label12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ctr = 0
    frame1.destroy()
    frame1 = Frame(window)
    frame1.pack(side=TOP, pady=0)
    label8 = Label(window, bg='green', text=str(ctr))
    label8.place(x=5, y=5)
    label15 = Label(window, bg='white', height=4, width=100, anchor=S, text="                             Process             State ", )
    label15.place(x=150, y=0)
    for i in range(0, procNo):
        label[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label7[i] = Label(label[i], bg='grey', width=10, height=2, text="Not arrived")
        label[i].grid(row=2 * i, column=100)
        label7[i].grid()
    for i in range(0, procNo):
        label12[i] = Label(frame1, bg='black', width=11, height=3, pady=2)
        label13[i] = Label(label12[i], bg='red', width=10, height=2, text="Process" + str(i+1))
        label12[i].grid(row=2 * i, column=0)
        label13[i].grid()
    label16 = Label(window, bg='light blue', height=5, width=150, anchor=N, text="When a procedure enters the condition of running, the condition of that procedure is not erased from the scheduler until it completes its administration time. A non-pre-emptive scheduler\nrelies on threads to voluntarily yield its execution context for another thread to run. A thread may yield its execution context in order to wait on a synchronization event like a\nlock/semaphore/barrier or an IO event like arrival of data from disk or network. When we consider modern multicore CPUs, there are more than one hardware entities available to execute a\ngiven thread. Often this means there will be no practical difference between a pre-emptive and a non-pre-emptive scheduler as long as there are no malicious threads that use up all\nexecution resources and never complete execution without waiting on an IO event.")
    label16.place(x=18, y=500)

    maxi=-1
    mini=-1
    mini1=1000
    x=0
    read_process(procNo)
    for i in range(0,procNo):
        for j in range(0,procNo-i-1):
            if prolist[j].at>prolist[j+1].at:
                prolist[j],prolist[j+1]=prolist[j+1],prolist[j]

    timer=0
    timer=timer + prolist[0].at
    for j in range(0, prolist[0].at):
        label8.config(text=str(ctr))
        ctr = ctr + 1
        for e in range(0, procNo):
            if (prolist[e].at <= ctr):
                label7[e].config(bg="grey", text="not arrived")
        window.update()
        time.sleep(1)
    c=prolist[0].at

    for j in range (0,procNo):
        maxi=-1
        for i in range(0,procNo):
            if (prolist[i].pri>maxi) and (prolist[i].at<=c) and (prolist[i].flag==-1):
                maxi = prolist[i].pri
                mini=i
        if (maxi==-1):
            x=mini
            for i in range(0,procNo):
                if (prolist[i].at<=mini1) and (prolist[i].flag==-1):
                    mini1=prolist[i].at
                    mini=i
            timer=timer+prolist[mini].at-prolist[x].ct

        timer = timer + prolist[mini].bt
        prolist[mini].ct=c+prolist[mini].bt
        prolist[mini].tat=prolist[mini].ct-prolist[mini].at
        prolist[mini].wt=prolist[mini].tat-prolist[mini].bt
        prolist[mini].flag=0
        c=prolist[mini].ct
        avgwt+=prolist[mini].wt
        avgtat+=prolist[mini].tat
        for k in range(0, prolist[mini].bt):
            label7[mini].config(bg="blue", text="Running")
            ctr += 1
            window.update()
            for e in range(0, procNo):
                if (prolist[e].at <= ctr and prolist[e].flag == -1 and e!=mini):
                    label7[e].config(bg="yellow", text="in queue")
                    window.update()
            label8.config(text=str(ctr))
            window.update()
            time.sleep(1)
        label7[mini].config(bg="green", text="Done")
        messagebox.showinfo("Process-" + str(mini+1) + " completed",
                            " completion time=" + str(timer) + "\nturn around time=" + str(
                                prolist[mini].tat) + "\nwaiting time=" + str(prolist[mini].wt))
        prolist[mini].flag=0

    avgwt/=procNo
    avgtat/=procNo
    #print "Process\tAT\tBT\tCT\tTAT\tWT"
    for i in range(0,procNo):
        print (prolist[i].pno,prolist[i].at,prolist[i].bt,prolist[i].ct,prolist[i].tat,prolist[i].wt)
    print ("Average Waiting time: ",avgwt)
    print ("Average turn around time: ",avgtat)




def nextPage(event):
    global avgtat
    global avgwt
    global prolist
    global procMax
    global page
    global resNo
    global frame1
    global label2
    global procNo
    global procMaxNo
    global but2
    if page == 1:
        if resNo == 0:
            messagebox.showerror(title="Resource Manager", message="Add atleast one resource to continue")
        else:
            label16.destroy()
            msg = messagebox.askokcancel(title="Resource Manager", message="Do you want to continue?")
            if msg == True:
                x=[]
                page = page + 1
                frame1.destroy()
                frame1 = Frame(window)
                frame1.pack(side=TOP, pady=30)
                label2 = Label(frame1, text="Enter process data)", relief=RIDGE,
                               font=fontSmall)
                procNo = tkSimpleDialog.askinteger("Process Scheduling", "Enter number of processes")
                for i in range(0,int(procNo)):
                    procMax[i][0]=tkSimpleDialog.askinteger("Process"+str(i+1), "Enter arrival time")
                    procMax[i][1]=tkSimpleDialog.askinteger("Process"+str(i+1), "Enter burst time")
                    procMax[i][2]=tkSimpleDialog.askinteger("Process"+str(i+1), "Enter priority time")
                        
   
                
                
                

    elif page == 2:
        if procNo == 0:
            messagebox.showerror(title="Process Manager", message="Add atleast one process to continue")
        else:
            msg = messagebox.askokcancel(title="Process Manager", message="Do you want to continue?")
            if msg == True:
                page = page + 1
                frame1.destroy()
                frame1 = Frame(window)
                frame1.pack(side=TOP, pady=30)

                but2 = Button(frame1, text="  SJF  ", command=sjf)
                but2.grid(row=1, column=0)

                but3 = Button(frame1, text="  RR   ", command=rr)
                but3.grid(row=1, column=1)

                but4 = Button(frame1, text="     PREEMPTIVE PRIORITY     ", command=pp)
                but4.grid(row=1, column=2)

                but5 = Button(frame1, text="FCFS ", command=fcfs)
                but5.grid(row=2, column=0)

                but6 = Button(frame1, text=" SRTF", command=srtf)
                but6.grid(row=2, column=1)

                but7 = Button(frame1, text="NON PREEMPTIVE PRIORITY", command=nonpri)
                but7.grid(row=2, column=2)




window = Toplevel()
fontHead = Font(family="Helvetica", size=20)

fontSmall = Font(family="Helvetica", size=15)
image = Image.open("pic1.jpg")
window.geometry("1250x656")
window.resizable(width=False, height=False)

bgimage = ImageTk.PhotoImage(image)

bglabel = Label(window, image=bgimage)

bglabel.place(x=0, y=0)

label1 = Label(window, text="Process Scheduling", font=fontHead)
label1.pack(pady=10, side=TOP)

label16 = Label(window, bg='light blue', height=17, width=150, anchor=N, text="Process Scheduling\nThe process scheduling is the activity of the process manager that handles the removal of the running process from the CPU and the selection of another process on the basis of a\nparticular strategy.Process scheduling is an essential part of a Multiprogramming operating systems. Such operating systems allow more than one process to be loaded into the\nexecutable memory at a time and the loaded process shares the CPU using time multiplexing.\n\nProcess Scheduling Queues\nThe OS maintains all PCBs in Process Scheduling Queues. The OS maintains a separate queue for each of the process states and PCBs of all processes in the same execution state are placed in\nthe same queue. When the state of a process is changed, its PCB is unlinked from its current queue and moved to its new state queue.\n\nThe Operating System maintains the following important process scheduling queues:\n.1.Job queue − This queue keeps all the processes in the system.\n.2.Ready queue − This queue keeps a set of all processes residing in main memory, ready and waiting to execute. A new process is always put in this queue.\n.3.Device queues − The processes which are blocked due to unavailability of an I/O device constitute this queue.\n\nThe OS can use different policies to manage each queue (FIFO, Round Robin, Priority, etc.). The OS scheduler determines how to move processes between the ready and\nrun queues which can onlyhave one entry per processor core on the system; in the above diagram, it has been merged with the CPU.\n",)
label16.place(x=18, y=350)

frame1 = Frame(window)
frame1.pack(side=TOP, pady=30)

nextLabel = Label(window, text="Press \'Enter\' to continue", font=fontSmall)
nextLabel.pack(side=BOTTOM)

window.bind("<Return>", nextPage)

page = 1

resNo = 3

resLabel = []
resScroll = []

procNo = 0

procMaxLabel = []
procAlloc = []
procLabel = []
procScroll = []

window.mainloop()

from tkinter.ttk import *