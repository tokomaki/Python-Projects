import colorama, datetime, os, shlex, signal, subprocess, sys, time

def run(command_chain, timeout = 30):
    """
    Runs the specified command chain and returns (True, <output>) on success. 
    If the command doesn't return within the specified time (in seconds), 
    (False, "") is returned. 
    """

    command_list = command_chain.split("|")
    start = datetime.datetime.now()
    process = None
    for command in command_list:
        tokens = shlex.split(command.strip())
        program = []
        for token in tokens:
            if token == "<" or token == ">":
                break
            program.append(token)
        stdin = None if not "<" in tokens \
                else open(tokens[tokens.index("<") + 1], "r")
        stdout = subprocess.PIPE if not ">" in tokens \
                 else open(tokens[tokens.index(">") + 1], "w")
        if process == None:
            process = subprocess.Popen(program, stdin = stdin, 
                                       stdout = stdout, 
                                       stderr = subprocess.STDOUT)
        else:
            process = subprocess.Popen(program, stdin = process.stdout, 
                                       stdout = stdout, 
                                       stderr = subprocess.STDOUT)
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return False, ""
    return (True, process.stdout.read().strip().replace("\r\n", "\n")) \
        if process.stdout != None else (True, "")
    
def ok():
    """
    Returns the string "Pass" in green.
    """
    return "%sPass" %(colorama.Fore.GREEN)

def notok():
    """
    Returns the string "Fail" in red.
    """

    return "%sFail" %(colorama.Fore.RED)

def Problem1():
    print "***** Wind Chill *****"
    command = "python wind_chill.py 32 15"
    sought = """21.5889888905"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem2():
    print "***** Body Mass Index *****"
    command = "python bmi.py 75 1.83"
    sought = """22.3954134193"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem3():
    print "***** Polar Coordinates *****"
    command = "python polar.py 1 1"
    sought = """1.41421356237
0.785398163397"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem4():
    print "***** Order Check *****"
    command = "python order_check.py 2 4 5"
    sought = """True"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python order_check.py 2 7 6"
    sought = """False"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python order_check.py 7 3 1"
    sought = """True"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python order_check.py 7 3 4"
    sought = """False"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem5():
    print "***** Day of the Week *****"
    command = "python day_of_week.py 3 14 1879"
    sought = """5"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem6():
    print "***** Mercator Projection *****"
    command = "python mercator.py 0 42.36 -71.06"
    sought = """-71.06 0.817646151942"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem7():
    print "***** Great Circle *****"
    command = "python great_circle.py 48.87 -2.33 37.8 -122.4"
    sought = """8701.38954324"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem8():
    print "***** Three Sort *****"
    command = "python three_sort.py 1 2 3"
    sought = """1 2 3"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python three_sort.py 1 3 2"
    sought = """1 2 3"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python three_sort.py 2 1 3"
    sought = """1 2 3"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python three_sort.py 2 3 1"
    sought = """1 2 3"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python three_sort.py 3 1 2"
    sought = """1 2 3"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))
    command = "python three_sort.py 3 2 1"
    sought = """1 2 3"""
    got = run(command)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem9():
    print "***** Random Integer *****"
    command = "python random_int.py 10 20"
    sought = """Random integer from [10, 20)"""
    got = int(run(command)[1])
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got >= 10 and got < 20 else "Got:\n%s\n%s" %(got, notok()))

def Problem10():
    print "***** Three Dice *****"
    command = "python three_dice.py"
    sought = """Random integer from [3, 18]"""
    got = int(run(command)[1])
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got >= 3 and got <= 18 else "Got:\n%s\n%s" %(got, notok()))

if __name__ == "__main__":
    colorama.init(autoreset = True)
    problems = [None, Problem1, Problem2, Problem3, Problem4, Problem5, 
                Problem6, Problem7, Problem8, Problem9, Problem10]
    args = map(int, sys.argv[1:])
    args = args if len(args) > 0 else range(1, len(problems))
    for i in args:
        problems[i]()
        print ""
