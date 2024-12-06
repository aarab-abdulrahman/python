# client (code)

` HOST = '192.168.x.x' `

### 1. Verify the Server's IP Address Run the following command on the server to identify its local IP address:

- open terminal 
- Run the following command on the server to identify its local IP address:

***windows***
```bash
ipconfig
```
***linux / macOS***
```bash
ifconfig
```
- check  your primary ` IPv4 address `

### 2. Check Firewall Settings

***windows***

**Step 1: Open Windows Firewall Settings**
1. Press ` Win + R ` to open the Run dialog box.
2. Type firewall.cpl and press Enter. This opens the Windows Firewall settings.

**Step 2: Allow an App or Port Through the Firewall**
1. In the left-hand menu, click "Advanced settings". This opens the Windows Defender Firewall with Advanced Security window.
2. In the left-hand pane, click Inbound Rules.
3. In the right-hand pane, click "New Rule...".

**Step 3: Create a Rule for the Port**
1. Select Port and click Next.
2. Choose TCP or UDP (your script uses TCP), and specify ` 12345 ` in the "Specific local ports" field. Click Next.
3. Select Allow the connection and click Next.
4. Choose when the rule applies:
    - **Domain:** Applies when connected to a corporate domain.
    - **Private:** Applies when connected to a private network (like your home Wi-Fi).
    - **Public:** Applies when connected to public Wi-Fi.
(For most setups, select Private and Public.)
5. Name the rule (e.g., Chatroom Server Port 12345) and click Finish.

___

***Linux (Ubuntu)***
**Step 1: Check the Firewall Status**

1. Open a terminal
2. Run the command:
    ```bash
    Copy code
    ```
    - If the firewall is inactive, you can enable it with:

    ```bash
    sudo ufw enable
    ```
**Step 2: Allow Incoming Traffic on the Port**

1. Allow traffic for port 12345:
    ```bash
    sudo ufw allow 12345/tcp
    ```
2. Verify the rule was added:
    ```bash
    sudo ufw status
    ```
**Step 3: Restart the Firewall**

 - If necessary, restart the firewall to apply changes:

    ```bash
    sudo ufw reload
    ```

___

***macOS***

**Step 1: Open Firewall Settings**
1. Go to System Preferences > Security & Privacy.
2. Click the Firewall tab.
3. If the Firewall is off, turn it on.

**Step 2: Add a Rule**
1. Click Firewall Options... or Advanced....
2. Click the "+" button to add a new rule.
3. Navigate to your Python executable or specify the port manually using a custom rule.

**Step 3: Save and Apply Changes**
 - Save the changes, and the firewall will now allow connections on the specified port.
