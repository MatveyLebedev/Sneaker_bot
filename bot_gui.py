import s_bot
import time
import tkinter as tk
from threading import Thread
from multiprocessing import Process

if __name__ == '__main__':

    root = tk.Tk()
    frame = tk.Frame(root)
    root.configure(bg="aqua")

    stop_batton = tk.Button(text='start', bg='red', width=40, height=2)
    set_batton = tk.Button(text='settings', bg='black', width=40, height=2, fg='white')
    activyty_batton = tk.Button(text='generate_activity', bg='black', width=40, height=2, fg='white')

    log = tk.Label(bg='black', fg='red', width=40, height=5)

    def stop_prog(a):
        if s_bot.drive.stop_flag == False:
            s_bot.drive.stop_flag = True
            stop_batton['text'] = 'start'
        else:
            s_bot.drive.stop_flag = False
            stop_batton['text'] = 'stop'

    def update_inf():
        while 1 == 1:
            log['text'] = s_bot.drive.inf
            time.sleep(0.1)

    def activity(o):

        for i in range(len(s_bot.log)):
            try:
                s_bot.generare_activity(i)
                log['text'] = f'accaunt {i} prepard'
            except:
                log['text'] = f'error whith accaunt {i}'

    def open_settings(o):
        root_set = tk.Toplevel(root)
        root_set.title('settings')
        root_set.focus_set()
        frame_set = tk.Frame(root_set)
        frame_set.focus_set()
        root_set.configure(bg="aqua")

        sets = open('bot_settings.txt')
        sets = list(sets)

        card_number = sets[0].split(' ')[0]
        month = sets[1].split(' ')[0]
        year = sets[2].split(' ')[0]
        cvs = sets[3].split(' ')[0]
        target_URL = sets[4].split(' ')[0]
        size = ''
        for i in range(len(sets[5].split(' ')) - 3):
            size += sets[5].split(' ')[i]
            size += ' '

        key = sets[6].split(' ')[0]

        name_cn = tk.StringVar()
        name_cn.set(str(card_number))
        name_m = tk.StringVar()
        name_m.set(str(month))
        name_y = tk.StringVar()
        name_y.set(str(year))
        name_cvs = tk.StringVar()
        name_cvs.set(str(cvs))
        name_turl = tk.StringVar()
        name_turl.set(str(target_URL))
        name_tsize = tk.StringVar()
        name_tsize.set(str(size))
        name_lk = tk.StringVar()
        name_lk.set(str(key))

        l1 = tk.Label(root_set, text="Card Number", width=40, bg="black", font='white', fg='white')
        e1 = tk.Entry(root_set, width=40, bg="black", textvariable=name_cn, fg='white', font='white')
        l2 = tk.Label(root_set, text="Month", width=40, bg="black", font='white', fg='white')
        e2 = tk.Entry(root_set, width=40, bg="black", font='white', fg='white', textvariable=name_m)
        l3 = tk.Label(root_set, text="Year", width=40, bg="black", font='white', fg='white')
        e3 = tk.Entry(root_set, width=40, bg="black", font='white', fg='white', textvariable=name_y)
        l4 = tk.Label(root_set, text="CVC", width=40, bg="black", font='white', fg='white')
        e4 = tk.Entry(root_set, width=40, bg="black", font='white', fg='white', textvariable=name_cvs)
        l5 = tk.Label(root_set, text="Target URL", width=40, bg="black", font='white', fg='white')
        e5 = tk.Entry(root_set, width=40, bg="black", font='white', fg='white', textvariable=name_turl)
        l6 = tk.Label(root_set, text="Target size (3 element array)", width=40, bg="black", font='white', fg='white')
        e6 = tk.Entry(root_set, width=40, bg="black", font='white', fg='white', textvariable=name_tsize)
        l7 = tk.Label(root_set, text="license key", width=40, bg="black", font='white', fg='white')
        e7 = tk.Entry(root_set, width=40, bg="black", font='white', fg='white', textvariable=name_lk)
        ba = tk.Button(root_set, text="Apply", bg="yellow", width=40)

        def save(s):
            param = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get(), e7.get()]
            L = sets
            nl = L[0].split(' ')
            nl[0] = param[0]
            L[0] = ' '.join(nl)
            nl = L[1].split(' ')
            nl[0] = param[1]
            L[1] = ' '.join(nl)
            nl = L[2].split(' ')
            nl[0] = param[2]
            L[2] = ' '.join(nl)
            nl = L[3].split(' ')
            nl[0] = param[3]
            L[3] = ' '.join(nl)
            nl = L[4].split(' ')
            nl[0] = param[4]
            L[4] = ' '.join(nl)
            nl = L[5].split(' ')
            for i in range(len(nl) - 3):
                nl[i] = param[5].split(' ')[i]

            L[5] = ' '.join(nl)
            nl = L[6].split(' ')
            nl[0] = param[6]
            L[6] = ' '.join(nl)

            file = open('bot_settings.txt', 'w')
            file.writelines(L)
            file.close()
            root_set.destroy()

        l1.grid(column=0, row=0, pady=3)
        e1.grid(column=0, row=1)
        l2.grid(column=0, row=2, pady=3)
        e2.grid(column=0, row=3)
        l3.grid(column=0, row=4, pady=3)
        e3.grid(column=0, row=5)
        l4.grid(column=0, row=6, pady=3)
        e4.grid(column=0, row=7)
        l5.grid(column=0, row=8, pady=3)
        e5.grid(column=0, row=9)
        l6.grid(column=0, row=10, pady=3)
        e6.grid(column=0, row=11)
        l7.grid(column=0, row=12, pady=3)
        e7.grid(column=0, row=13)
        ba.grid(column=0, row=14, pady=3)

        ba.bind('<Button-1>', save)

        frame_set.grid()
        root_set.mainloop()


    set_batton.bind('<Button-1>', open_settings)
    stop_batton.bind('<Button-1>', stop_prog)
    activyty_batton.bind('<Button-1>', activity)

    frame.pack()
    frame.focus_set()

    stop_batton.pack(pady=3)
    set_batton.pack()
    activyty_batton.pack(pady=3)
    log.pack(pady=3)


    update_log = Thread(target=update_inf)

    def main_pipe():
       s_bot.start_main()

    update_log.start()
    main = Thread(target=main_pipe)
    main.start()

    root.mainloop()