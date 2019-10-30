/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package java_gui;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.net.InetAddress;
import java.net.Socket;

// Sends data from GUI to Python Controller
public class Client {

    private static Socket socket;
    private final String host = "localhost";

    //Port for sending data to Python controller
    private final int port = 65431;

    InetAddress address;
    
    String result = "";


    public Client() {

    }

    public void connectToServer() {
        try {
            address = InetAddress.getByName(host);
            socket = new Socket(address, port);

        } catch (Exception exception) {
            exception.printStackTrace();
        }

    }

    public void sendMessage(String messageToPython) {

        try {
            //Send the message to the server
            OutputStream os = socket.getOutputStream();
            OutputStreamWriter osw = new OutputStreamWriter(os);
            BufferedWriter bw = new BufferedWriter(osw);


            bw.write(messageToPython);
            bw.flush();

            
            
            //Get the return message from the server
            InputStream is = socket.getInputStream();
            InputStreamReader isr = new InputStreamReader(is);
            BufferedReader br = new BufferedReader(isr);
            
            
            result = br.readLine();
            System.out.println("Message received from the server : " +result);

        } catch (Exception exception) {
            exception.printStackTrace();
        }
    }

    public void closeSocket() {
        //Closing the socket
        try {
            socket.close();
        } catch (Exception e) {
            e.printStackTrace();
        }

    }
}
