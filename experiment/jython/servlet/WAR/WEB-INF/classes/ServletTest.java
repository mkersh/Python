import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class ServletTest extends HttpServlet {
	public void doGet (HttpServletRequest request,
					   HttpServletResponse response)
		throws ServletException, IOException {
		doPost(request, response);
	} 

	public void doPost (HttpServletRequest request,
					   HttpServletResponse response)
		throws ServletException, IOException {
		response.setContentType ("text/html");
		PrintWriter toClient = response.getWriter();
		toClient.println ("<html><head><title>Servlet Test</title>" +
						  "<body><h1>Servlet Test</h1></body></html>");
	}
}
