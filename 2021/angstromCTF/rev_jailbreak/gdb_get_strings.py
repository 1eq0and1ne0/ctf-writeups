import gdb

gdb.execute('break *0x555555554000+0x1631')
gdb.execute('run')

gdb.execute('set $eip=0x555555554000+0x1620')
for i in range(40):
    gdb.execute(f'echo STR {i}: ')
    gdb.execute(f'set $rdi={i}')
    gdb.execute('set $rip=0x555555554000+0x1620')
    gdb.execute('continue')


# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 0:What would you like to do?

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 1:Welcome to clam's daring jailbreak! Please keep your hands and feet inside the jail at all times.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 2:look around

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 3:You look around your cell and you see an old bed along with a snake. Outside, kmh stares at you, wondering how to make the jail cell more contrived.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 4:You're speaking nonsense. Cut that out.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 5:It seems that clam won't be escaping today.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 6:sleep

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 7:You lie down on the bed and close your eyes. You then get bitten by the snake. What did you expect to happen when you went to bed next a snake?

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 8:You look around your cell and you see an old bed along with a snake. Outside, kmh is nowhere to be seen.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 9:knock on the wall

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 10:You here a muffled voice from the other side saying "I shouldn't have blatantly ripped off pico's challenges..."

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 11:pry the bars open

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 12:You start prying the prison bars open. Realizing this is unintended, kmh decides to patch the universe interpreter to make the bars immovable.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 13:You start prying the prison bars open. A wide gap opens and you slip through.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 14:throw the snake at kmh

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 15:pick the snake up

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 16:You pick the snake up.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 17:You throw the snake at kmh and watch as he runs in fear.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 18:You look around and see that kmh has already made the jail contrived! There's a red button and a green button with a sign that says "pres butons 2 get fleg".

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 19:press the red button

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 20:press the green button

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 21:You pressed the red button. Nothing changed.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 22:You pressed the green button. Nothing changed.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 23:bananarama

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 24:For some reason, a flag popped out of the wall, and you walk closer to read it.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 25:flag.txt

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 26:r

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 27:Couldn't find flag file.

# Breakpoint 1, 0x0000555555555631 in ?? ()
# STR 28:Attached to the flag is a key to the front door. It looks like clam is escaping after all.

