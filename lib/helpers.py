import time
import os
import curses

def car_animation(speed):
    
    frame1 = """
      ______
     /|_||_\`.__
    (   _    _ _|
    =`-(_)--(_)-'
    """

    frame2 = """
        ______
       /|_||_\`.__
      (   _    _ _|
      =`-(_)--(_)-'
    """

    frame3 = """
          ______
         /|_||_\`.__
        (   _    _ _|
        =`-(_)--(_)-'
    """

    frame4 = """
            ______
           /|_||_\`.__
          (   _    _ _|
          =`-(_)--(_)-'
    """

    frame4 = """
              ______
             /|_||_\`.__
            (   _    _ _|
            =`-(_)--(_)-'
    """

    frame5 = """
                ______
               /|_||_\`.__
              (   _    _ _|
              =`-(_)--(_)-'
    """

    frame6 = """
                  ______
                 /|_||_\`.__
                (   _    _ _|
                =`-(_)--(_)-'
    """

    frame7 = """
                    ______
                   /|_||_\`.__
                  (   _    _ _|
                  =`-(_)--(_)-'
    """

    frame8 = """
                      ______
                     /|_||_\`.__
                    (   _    _ _|
                    =`-(_)--(_)-'
    """

    frame9 = """
                        ______
                       /|_||_\`.__
                      (   _    _ _|
                      =`-(_)--(_)-'
    """

    frame10 = """
                          ______
                         /|_||_\`.__         
                        (   _    _ _|          
                        =`-(_)--(_)-'         
    """

    frame11 = """
                            ______
                           /|_||_\`.__         
                          (   _    _ _|          
                          =`-(_)--(_)-'         
    """
    
    frame12 = """
                              ______
                             /|_||_\`.__         
                            (   _    _ _|          
                            =`-(_)--(_)-'         
    """
    frame13 = """
                                ______
                               /|_||_\`.__         
                              (   _    _ _|          
                              =`-(_)--(_)-'         
    """



    frame14 = """
                                  ______
                                 /|_||_\`.__         
                                (   _    _ _|          
                                =`-(_)--(_)-'         
    """
    frame15 = """
                                    ______
                                   /|_||_\`.__       
                                  (   _    _ _|        
                                  =`-(_)--(_)-'       
    """
    frame16 = """
                                      ______
                                     /|_||_\`.__     
                                    (   _    _ _|      
                                    =`-(_)--(_)-'     
    """
    frame17 = """
                                        ______
                                       /|_||_\`.__   
                                      (   _    _ _|    
                                      =`-(_)--(_)-'   
    """
    frame18 = """
                                          ______
                                         /|_||_\`.__ 
                                        (   _    _ _|  
                                        =`-(_)--(_)-' 
    """
    frame19 = """                                       
                                          ______         
                                         /|_||_\`.__  
                                        (   _    _ _|
                                        =`-(_)--(_)-'
    """
    frame20 = """                                       
                                            ______         
                                           /|_||_\`.__  
                                          (   _    _ _|
                                          =`-(_)--(_)-'
    """

    frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16, frame17, frame18, frame19, frame20]

    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(speed)

def car_crash_animation(speed):

    frame1 = """
      ______
     /|_||_\`.__
    (   _    _ _|
    =`-(_)--(_)-'
    """

    frame2 = """
        ______
       /|_||_\`.__
      (   _    _ _|
      =`-(_)--(_)-'
    """

    frame3 = """
          ______
         /|_||_\`.__
        (   _    _ _|
        =`-(_)--(_)-'
    """

    frame4 = """
            ______
           /|_||_\`.__
          (   _    _ _|
          =`-(_)--(_)-'
    """

    frame4 = """
              ______
             /|_||_\`.__
            (   _    _ _|
            =`-(_)--(_)-'
    """

    frame5 = """
                ______
               /|_||_\`.__
              (   _    _ _|
              =`-(_)--(_)-'
    """

    frame6 = """
                  ______
                 /|_||_\`.__
                (   _    _ _|
                =`-(_)--(_)-'
    """

    frame7 = """
                    ______
                   /|_||_\`.__
                  (   _    _ _|
                  =`-(_)--(_)-'
    """

    frame8 = """
                      ______
                     /|_||_\`.__
                    (   _    _ _|
                    =`-(_)--(_)-'
    """

    frame9 = """
                        ______
                       /|_||_\`.__
                      (   _    _ _|
                      =`-(_)--(_)-'
    """
    frame10 = """
                          ______
                         /|_||_\`.__         
                        (   _    _ _|          
                        =`-(_)--(_)-'         
    """

    frame11 = """
                            ______
                           /|_||_\`.__         
                          (   _    _ _|          
                          =`-(_)--(_)-'         
    """
    
    frame12 = """
                              ______
                             /|_||_\`.__         
                            (   _    _ _|          
                            =`-(_)--(_)-'         
    """
    
    frame13 = """
                                ______
                               /|_||_\`.__         
                              (   _    _ _|          
                              =`-(_)--(_)-'         
    """
    
    frame14 = """
                                  ______
                                 /|_||_\`.__         
                                (   _    _ _|          
                                =`-(_)--(_)-'         
    """

    frame15 = """
                                    ______
                                   /|_||_\`.__         \ O /
                                  (   _    _ _|          |
                                  =`-(_)--(_)-'         / |
    """
    frame16 = """
                                      ______
                                     /|_||_\`.__       \ O /
                                    (   _    _ _|        |
                                    =`-(_)--(_)-'       / |
    """
    frame17 = """
                                        ______
                                       /|_||_\`.__     \ O /
                                      (   _    _ _|      |
                                      =`-(_)--(_)-'     / |
    """
    frame18 = """
                                          ______
                                         /|_||_\`.__   \ O /
                                        (   _    _ _|    |
                                        =`-(_)--(_)-'   / |
    """
    frame19 = """
                                            ______
                                           /|_||_\`.__ \ O /
                                          (   _    _ _|  |
                                          =`-(_)--(_)-' / |
    """
    frame20 = """                                       
                                            ______         
                                           /|_||_\`.__   
                                          (   _    _ _| \___/#?!
                                          =`-(_)--(_)-' /   |
    """

    frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16, frame17, frame18, frame19, frame20]

    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(speed)

import time
import curses


def loading():
    
    frame1 = """
     
     
                    -  Loading  -
     
        Copyright (c) 1983 by Flatiron Systems, Inc.
        
    """

    frame2 = """
     
     
                    X  Loading  X
     
        Copyright (c) 1983 by Flatiron Systems, Inc.
    
    """

    frame3 = """
     
     
                    |  Loading  |
     
        Copyright (c) 1983 by Flatiron Systems, Inc. 
    
    """

    frame4 = """
     
     
                    X  Loading  X
                    
        Copyright (c) 1983 by Flatiron Systems, Inc.
    
    """

    frame5 = """
     
     
                    -  Loading  -
     
        Copyright (c) 1983 by Flatiron Systems, Inc.
    
    """
    
    frames = [frame1, frame2, frame3, frame4, frame5]
    for frame in frames:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(frame)
        time.sleep(.5)

def print_goodbye():
    print(' ')
    print(' ')
    print('   ____                 _ _                _     ')
    print('  / ___| ___   ___   __| | |__  _   _  ___| |    ')
    print(' | |  _ / _ \ / _ \ / _` | |  \| | | |/ _ \ |    ')
    print(' | |_| | (_) | (_) | (_| | |_) | |_| |  __/_|    ')
    print('  \____|\___/ \___/ \__,_|_.__/ \__, |\___(_)    ')
    print('                                |___/            ')
    print(' ')
    print(' ')