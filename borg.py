#!/usr/bin/env python3

import json
import argparse

def parsearg(args):
    parser = argparse.ArgumentParser(
             description='Borg (short for Be Organized)', prog='Borg')

class Borg():
    
    def __init__(self, filepath):
        self.data = self.get_json(filepath)

    def __len__(self):
        return(len(self.data))

    def __repr__(self):
        for keys in self.data:
           pass 
    
    """ 
    Create the file if it does not already exist
    """
    def get_json(self, filepath):
        with open('data.json') as data:
            return json.load(data)
    
    def display(self):
        print('')
        for keys in self.data:
            print('[{}] {}\n  - {}\n'.format(
                keys['isdone'], 
                keys['name'],
                keys['description']))


def main():
    todo = Borg('data.json') 

    todo.display()

if __name__ == '__main__':
    main()
