from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    print(recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    print(recv1)
    if recv1[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailfrom = 'MAIL FROM: <alice@me.com>\r\n'
    clientSocket.send(mailfrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    print('mailfrom response: ', recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptto = 'RCPT TO: <bob@me.com>\r\n'
    clientSocket.send(rcptto.encode())
    recv3 = clientSocket.recv(1024).decode()
    print('rcptto response: ', recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    # clientSocket.send('DATA'.encode())
    data = 'DATA\r\n.\r\n'
    clientSocket.send(data.encode())
    recv4 = clientSocket.recv(1024).decode()
    print('DATA response: ', recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    msgdata = 'Hi Bob, please stop emailing me.\r\n'
    clientSocket.send(msgdata.encode())
    recv5 = clientSocket.recv(1024).decode()
    print('msgdata response: ', recv5)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    msgend = '.\r\n'
    clientSocket.send(msgend.encode())
    recv6 = clientSocket.recv(1024).decode()
    print(recv6)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quit = 'QUIT\r\n'
    clientSocket.send(quit.encode())
    recv7 = clientSocket.recv(1024).decode()
    print(recv7)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')