# Basic execution of a

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from SimpleChain import SimpleChain
import time


def main():
    secondsUntilNext = 1 # normally 10 minutes, or 600 seconds
    c = SimpleChain()  # Start a chain
    for i in range(1, 20 + 1):
        time.sleep(secondsUntilNext)
        #print("Adding a new block. . .")
        c.add_block(f'This is block {i} of my first chain.')

    print(c.blocks[3].timestamp)
    print(c.blocks[7].data)
    print(c.blocks[9].hash)

    print(c.get_chain_size())
    print(c.verify())

    return c.verify()


if __name__ == "__main__":
    status = "An error may have occurred."
    result = main()
    if result == True:
        status = "Exiting properly."
    else:
        status = "An error occurred during execution."

print(status)
