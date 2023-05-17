class TambolaGame:
    """
    This class is a tambola game simulator
    Input: tambola ticket, input of numbers that are called out until now, input of claims made per chance.
    Output: list of claims validity per chance
    NOTE: The size of input list claims per chance is equal to size of numbers called out
    """

    @staticmethod
    def simulate_game(ticket, inp, claims_per_chance):
        valid_claims_per_chance = list()
        ts = TambolaState(ticket)

        for i in range(len(inp)):
            print("Number call: ", inp[i])
            ts.cross_number(inp[i])

            claim = claims_per_chance[i]
            if not claim:
                valid_claims_per_chance.append(None)
                continue

            print('Claim made: ', claim)
            cl_valid = ts.claim_validator(claim)

            if cl_valid:
                valid_claims_per_chance.append('ACCEPTED')
                print('ACCEPTED')
                continue
            valid_claims_per_chance.append('REJECTED')
            print('REJECTED')
        return valid_claims_per_chance


class TambolaState:
    """
    This Class encapsulates current state of the game. Keeps track of ticket
    input: tambola ticket
    """
    def __init__(self, ticket):
        self.ticket = ticket
        self.crossed_numbers = []

    def cross_number(self, num):
        for i in range(0, len(self.ticket)):
            for j in range(0, len(self.ticket[0])):
                if self.ticket[i][j] == '_':
                    continue
                if self.ticket[i][j] == num:
                    self.ticket[i][j] = str(int(self.ticket[i][j])*-1)
                    self.crossed_numbers.append([i,j])

    def claim_validator(self, claim):
        """
        At a particular chance, claim can be validated.
        Rules: A player's claim to victory is only valid if it is made immediately following the announcement of the number that completes their winning sequence.
        :param claim: claim made
        :return: if the claim is valid
        """
        if claim == 'TOP_ROW':
            res = self.check_for_line(0)
        elif claim == 'MID_ROW':
            res = self.check_for_line(1)
        elif claim == 'LAST_ROW':
            res = self.check_for_line(2)
        elif claim == 'EARLY_FIVE':
            res = self.check_for_early_five()
        elif claim == 'FULL_HOUSE':
            res = self.check_full_house()
        return res

    def check_for_line(self, line):
        last_crossed_num = self.crossed_numbers.pop()
        if last_crossed_num[0] != line:
            return False

        flag = True
        for i in self.ticket[line]:
            if i == '_' or int(i) < 0:
                continue
            else:
                flag = False
                break
        return flag

    def check_for_early_five(self):
        if len(self.crossed_numbers) == 5:
            return True
        return False

    def check_full_house(self):
        for i in range(0, len(self.ticket)):
            for j in range(0, len(self.ticket[0])):
                if self.ticket[i][j] == '_':
                    continue
                if int(self.ticket[i][j]) > 0:
                    return False
        return True



