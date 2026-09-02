// ==============================================================================
// PROJECT: OPTIMUS JARVIS SUPER-FRAME
// PHASE: 86 (AUTOBOTS MICRO-CONTROLLER PULSE LOGIC & FIRMWARE ENGINE)
// OWNER: MASTER DEEPAK
// LANGUAGE: EMBEDDED C++ (FOR ARDUINO / ESP32 HARDWARE CHIP)
// MODE: 100% FUNCTIONAL HARDWARE CONTROL CODE
// ==============================================================================

#include <stdio.h>

// 1. हार्डवेयर पिंस का निर्धारण (Designing Input/Output Pins)
const int FORWARD_PIN  = 12; // रिमोट का आगे जाने वाला बटन पॉइंट
const int REVERSE_PIN  = 14; // रिमोट का पीछे जाने वाला बटन पॉइंट
const int LEFT_PIN     = 27; // रिमोट का बाएं जाने वाला बटन पॉइंट
const int RIGHT_PIN    = 26; // रिमोट का दाएं जाने वाला बटन पॉइंट

void setup() {
    // पिंस को आउटपुट मोड में सेट करना ताकि हम करंट भेज सकें
    pinMode(FORWARD_PIN, OUTPUT);
    pinMode(REVERSE_PIN, OUTPUT);
    pinMode(LEFT_PIN, OUTPUT);
    pinMode(RIGHT_PIN, OUTPUT);
    
    // शुरुआत में सभी सिग्नल्स को बंद रखना (Safety Gate)
    digitalWrite(FORWARD_PIN, LOW);
    digitalWrite(REVERSE_PIN, LOW);
    digitalWrite(LEFT_PIN, LOW);
    digitalWrite(RIGHT_PIN, LOW);
    
    Serial.begin(115200);
    Serial.println("Jarvis Hardware Firmware Initialized. Awaiting Master Deepak's Signals...");
}

// 2. गाड़ी को अपनी कोडिंग के अनुसार चलाने का मुख्य लॉजिक (Custom Design Logic)
void execute_movement(char command) {
    // चलने से पहले पुराने सभी सिग्नल्स को न्यूट्रल करना ताकि गियर्स आपस में न टकराएं
    digitalWrite(FORWARD_PIN, LOW);
    digitalWrite(REVERSE_PIN, LOW);
    digitalWrite(LEFT_PIN, LOW);
    digitalWrite(RIGHT_PIN, LOW);

    switch(command) {
        case 'W': case 'w':
            Serial.println("Action: Actuating Forward Motors");
            digitalWrite(FORWARD_PIN, HIGH); // पिन 12 में 5V करंट भेजकर थार को आगे बढ़ाना
            break;
        case 'S': case 's':
            Serial.println("Action: Actuating Reverse Motors");
            digitalWrite(REVERSE_PIN, HIGH); // पिन 14 में करंट भेजकर थार को पीछे लाना
            break;
        case 'A': case 'a':
            Serial.println("Action: Turning Steering Left");
            digitalWrite(LEFT_PIN, HIGH);    // पिन 27 में करंट भेजकर पहियों को बाएं मोड़ना
            break;
        case 'D': case 'd':
            Serial.println("Action: Turning Steering Right");
            digitalWrite(RIGHT_PIN, HIGH);   // पिन 26 में करंट भेजकर पहियों को दाएं मोड़ना
            break;
        default:
            Serial.println("Action: Neutral Gates Engaged. Vehicles Stationary.");
            break;
    }
}

void loop() {
    // जब आपके ओप्पो मोबाइल के ब्लूटूथ या टर्मक्स से कोई अक्षर (W,S,A,D) इस चिप को मिलेगा
    if (Serial.available() > 0) {
        char incoming_signal = Serial.read();
        execute_movement(incoming_signal); // तुरंत मोटर को कमांड भेजना
    }
}
