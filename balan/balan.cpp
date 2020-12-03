package B2_TinhGTBTS;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.*;

public class Server {

	public static int getPriority(char c) {
		if (c == '(')
			return 0;
		else if (c == '+' || c == '-')
			return 1;
		return 2;
	}

	public static boolean isDigit(char c) {
		if (c >= '0' && c <= '9')
			return true;
		return false;
	}

	public static String getNumber(String str, int i) {
		String num = "";
		char c = str.charAt(i);
		while (c == '.' || (c >= '0' && c <= '9')) {
			num += c;
			if (i == str.length() - 1)
				break;
			i++;
			c = str.charAt(i);
		}
		;
		return num;
	}

	public static boolean isOperation(char c) {
		if (c == '-' || c == '+' || c == '/' || c == '*')
			return true;
		return false;
	}

	public static float cal(float nd1, float nd2, char op) throws Exception {
		switch (op) {
		case '+':
			return nd1 + nd2;
		case '-':
			return nd1 - nd2;
		case '*':
			return nd1 * nd2;
		case '/':
			if (nd2 == 0)
				throw new Exception();
			return nd1 / nd2;
		}
		return 0;
	}

	public static double posfix(String bt) throws Exception {
		Stack st = new Stack();
		Queue q = new ArrayDeque();
		for (int i = 0; i < bt.length(); i++) {
			char c = bt.charAt(i);
			if (isDigit(c) == true) {
				String num = getNumber(bt, i);
				i += num.length() - 1;
				q.offer(num);
			}

			else if (c == '(')
				st.push(c);
			else if (c == ')') {

				char topSt;
				do {
					topSt = (char) st.pop();
					if (topSt != '(')
						q.offer(topSt);

				} while (topSt != '(');
			} else if (isOperation(c)) {
				if (st.empty()) {
					st.push(c);
				} else {// B
					char topPeek = (char) st.peek();
					if (!isOperation(topPeek))
						st.push(c);
					else {
						if (getPriority(topPeek) < getPriority(c))
							st.push(c);
						else {
							while (!st.empty() && isOperation(topPeek)) {
								char topSt = (char) st.pop();
								q.offer(topSt);
							}
							;
							st.push(c);
						}
					}
				}

			}
		}

		while (!st.empty()) {
			char topSt = (char) st.pop();
			q.offer(topSt);
		}
		return calculator(st, q);
	}

	static double calculator(Stack st, Queue q) throws Exception {
		String temp;
		float p1, p2;
		while (!q.isEmpty()) {
			temp = q.poll().toString();
			if (!isOperation(temp.charAt(0))) {
				st.push(temp);
			} else {
				p1 = Float.parseFloat((String) st.pop());
				p2 = Float.parseFloat((String) st.pop());
				String tempCal = cal(p2, p1, temp.charAt(0)) + "";
				st.push(tempCal);
			}
		}
		return Double.parseDouble((String) st.peek());
	}

	public static void main(String[] args) throws Exception {

		ServerSocket server = new ServerSocket(9999);
		System.out.println("server is started");
		Socket socket = server.accept();
		DataOutputStream dos = new DataOutputStream(socket.getOutputStream());
		DataInputStream dis = new DataInputStream(socket.getInputStream());
		Double rs;
		while (true) {
			String ClientSms = dis.readUTF();
			System.out.println(ClientSms);
			rs = posfix(ClientSms);
			System.out.println(rs);
			String sendSms = ClientSms + " = " + rs.toString();
			dos.writeUTF(sendSms);
			dos.flush();

		}

	}
}
