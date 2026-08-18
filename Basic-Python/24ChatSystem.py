# Build a simple chat system using classes in Python
# Users can join a chat system, send messages, and leave the chat system. The chat system keeps track of users and messages.




class Message:
    message_count = 1

    def __init__(self,sender,content):
        self.sender = sender
        self.content = content
        self.message_id = Message.message_count
        Message.message_count += 1 
    def __str__(self):
        return f"Message ID: {self.message_id}, Sender: {self.sender.username}, Content: {self.content}" 

class ChatRoom:
    def __init__(self,name):
        self.name = name 
        self.messages = []
        self.users = [] 

    def add_user(self,user):
        self.users.append(user)

    def remove_user(self,user):
        for message in self.messages:
            if message.sender == user:
                self.messages.remove(message)
        self.users.remove(user)

    def broadcast_message(self,sender,content):
        message = Message(sender,content)
        self.messages.append(message)
    
    def show_chat_history(self):
        for message in self.messages:
            print(message) 

class User:
    def __init__(self,username):
        self.username = username
        self.chat_room = None

    def join_chat_room(self,chat_room):
        if self.chat_room:
            print(f"{self.username} is already in a chat room.")
            return
        self.chat_room = chat_room
        self.chat_room.add_user(self)
        print(f"{self.username} has joined the chat room:{self.chat_room.name}.")
    
    def leave_chat_room(self):
        if self.chat_room:
            print(f"{self.username} has left the chat room:{self.chat_room.name}.")
            self.chat_room.remove_user(self)
            self.chat_room = None
        else:
            print(f"{self.username} is not in a chat room.")
 
    def send_message(self,content):
        if self.chat_room:
            self.chat_room.broadcast_message(self,content)
        else:
            print(f"{self.username} is not in a chat room.")


#Example Usage

if __name__ == "__main__":
    chat_room = ChatRoom("MyChatSystem")
    user1 = User("Alice")
    user2 = User("Bob")

    user1.join_chat_room(chat_room)
    user2.join_chat_room(chat_room)

    user1.send_message("Hello, Everyon!")
    user2.send_message("Hi, Alice! How are you?")

    user3 = User("Charlie")
    user3.join_chat_room(chat_room)
    user3.send_message("Hey guys, what's up?")

    chat_room.show_chat_history()
    # print(chat_room.users)
    # print(chat_room.messages)
    user2.leave_chat_room()
    chat_room.show_chat_history()