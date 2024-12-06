# client (code)

<HOST = '192.168.x.x'>

### 1. Verify the Server's IP Address Run the following command on the server to identify its local IP address:

- open terminal 
- Run the following command on the server to identify its local IP address:

***windows***
```terminal
ipconfig
```
***linux / macOS***
```terminal
ifconfig
```
- check  your primary *** IPv4 address ***

### 2. Check Firewall Settings

***windows***
**Step 1: Open Windows Firewall Settings**
 1. Press <Win + R> to open the Run dialog box.
 2. Type firewall.cpl and press Enter. This opens the Windows Firewall settings.

**Step 2: Allow an App or Port Through the Firewall**
 1. In the left-hand menu, click "Advanced settings". This opens the Windows Defender Firewall with Advanced Security window.
 2. In the left-hand pane, click Inbound Rules.
 3. In the right-hand pane, click "New Rule...".
 
**Step 3: Create a Rule for the Port**
 1. Select Port and click Next.
 2. Choose TCP or UDP (your script uses TCP), and specify 12345 in the "Specific local ports" field. Click Next.
 3. Select Allow the connection and click Next.
 4. Choose when the rule applies:
    - **Domain:** Applies when connected to a corporate domain.
    - **Private:** Applies when connected to a private network (like your home Wi-Fi).
    - **Public:** Applies when connected to public Wi-Fi.
(For most setups, select Private and Public.)
 5. Name the rule (e.g., Chatroom Server Port 12345) and click Finish.


 ## git
 ```bash
    node app.js
 ```
