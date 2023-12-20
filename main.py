from instalike import LikingBot
import argparse

if __name__ == "__main__":
    # Set up argparse for command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("username", type=str, help="Username")
    parser.add_argument("password", type=str, help="Password")
    parser.add_argument("max_iter", type=int, help="Max iterations")
    args = parser.parse_args()

    # Access arguments using args.username, args.password, args.max_iter
    username = args.username
    password = args.password
    max_iter = args.max_iter

    # Rest of your script...
    bot = LikingBot(username, password, max_iter)
