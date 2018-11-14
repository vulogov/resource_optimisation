#!/usr/bin/env python3

import pulp

def main():
    model = pulp.LpProblem("Resource allocation monitoring with cost optimisation", pulp.LpMinimize)

if __name__ == "__main__":
    main()
