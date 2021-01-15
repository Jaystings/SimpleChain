from SimpleBlock import SimpleBlock
import datetime

class SimpleChain:
    def __init__(self):  # initialize when creating a chain
        self.blocks = [self.get_genesis_block()]


    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def get_genesis_block(self):
        return SimpleBlock(0,
                            datetime.datetime.utcnow(),
                            'Genesis',
                            'arbitrary')

    def add_block(self, data):
        self.blocks.append(SimpleBlock(len(self.blocks),
                                        datetime.datetime.utcnow(),
                                        data,
                                        self.blocks[len(self.blocks) - 1].hash))

    def get_chain_size(self):  # exclude genesis block
        return len(self.blocks) - 1

    def verify(self, verbose=True):
        flag = True
        for i in range(1, len(self.blocks)):
            if not self.blocks[i].verify():  # assume Genesis block integrity
                flag = False
                if verbose:
                    print(f'Wrong data type(s) at block {i}.')
            if self.blocks[i].index != i:
                flag = False
                if verbose:
                    print(f'Wrong block index at block {i}.')
            if self.blocks[i - 1].hash != self.blocks[i].previous_hash:
                flag = False
                if verbose:
                    print(f'Wrong previous hash at block {i}.')
            if self.blocks[i].hash != self.blocks[i].hashing():
                flag = False
                if verbose:
                    print(f'Wrong hash at block {i}.')
            if self.blocks[i - 1].timestamp >= self.blocks[i].timestamp:
                flag = False
                if verbose:
                    print(f'Backdating at block {i}.')
        return flag

    def fork(self, head='latest'):
        if head in ['latest', 'whole', 'all']:
            return copy.deepcopy(self)  # deepcopy since they are mutable
        else:
            c = copy.deepcopy(self)
            c.blocks = c.blocks[0:head + 1]
            return c

    def get_root(self, chain_2):
        min_chain_size = min(self.get_chain_size(), chain_2.get_chain_size())
        for i in range(1, min_chain_size + 1):
            if self.blocks[i] != chain_2.blocks[i]:
                return self.fork(i - 1)
        return self.fork(min_chain_size)