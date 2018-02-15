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
    print "***** Particle Identification *****"
    command = "python blob_finder.py 25 180.0 data/run_1/frame00001.jpg"
    sought = """13 Beads:
29 (214.7241, 82.8276)
36 (223.6111, 116.6667)
42 (260.2381, 234.8571)
35 (266.0286, 315.7143)
31 (286.5806, 355.4516)
37 (299.0541, 399.1351)
35 (310.5143, 214.6000)
31 (370.9355, 365.4194)
28 (393.5000, 144.2143)
27 (431.2593, 380.4074)
36 (477.8611, 49.3889)
38 (521.7105, 445.8421)
35 (588.5714, 402.1143)
15 Blobs:
29 (214.7241, 82.8276)
36 (223.6111, 116.6667)
1 (254.0000, 223.0000)
42 (260.2381, 234.8571)
35 (266.0286, 315.7143)
31 (286.5806, 355.4516)
37 (299.0541, 399.1351)
35 (310.5143, 214.6000)
31 (370.9355, 365.4194)
28 (393.5000, 144.2143)
27 (431.2593, 380.4074)
36 (477.8611, 49.3889)
38 (521.7105, 445.8421)
35 (588.5714, 402.1143)
13 (638.1538, 155.0000)"""
    got = run(command, 60)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

def Problem2():
    print "***** Particle Tracking *****"
    command = "python bead_tracker.py 25 180.0 25.0 data/run_1/%s" \
              %(" data/run_1/".join(sorted(os.listdir("data/run_1"))[:5]))
    sought = """7.1833
4.7932
2.1693
5.5287
5.4292
4.3962"""
    got = run(command, 60)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s\n..." %(sought)
    print "%s" %(ok() if got.startswith(sought) else "Got:\n%s\n%s" %(got, notok()))

def Problem3():
    print "***** Data Analysis *****"
    command = "python bead_tracker.py 25 180.0 25.0 data/run_1/%s | python avogadro.py" %(" data/run_1/".join(sorted(os.listdir("data/run_1"))))
    sought = """Boltzman = 1.253509e-23
Avogadro = 6.633037e+23"""
    got = run(command, 1800)[1]
    print "Command: %s" %(command)
    print "Sought:\n%s" %(sought)
    print "%s" %(ok() if got == sought else "Got:\n%s\n%s" %(got, notok()))

if __name__ == "__main__":
    colorama.init(autoreset = True)
    problems = [None, Problem1, Problem2, Problem3]
    args = map(int, sys.argv[1:])
    args = args if len(args) > 0 else range(1, len(problems))
    for i in args:
        problems[i]()
        print ""
