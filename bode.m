% Define the system constants
R1 = 8;      % ohms
L1 = 3.18e-3; % H
C1 = 3.31e-6; % F
R3 = 8;      % ohms
C2 = 49.74e-6; % F
L2 = 0.212e-3; % H
R2 = 8;      % ohms

% Define the s variable
s = tf('s');

% Low-Pass Filter (LPF)
LPF = R1 / (R1 + s*L1);
figure;
bode(LPF);
title('Bode Plot of Low-Pass Filter');

% High-Pass Filter (HPF)
HPF = s*R3*C1 / (1 + s*R3*C1);
figure;
bode(HPF);
title('Bode Plot of High-Pass Filter');

% Band-Pass Filter (BPF)
HPF_BPF = s*R2*C2 / (1 + s*R2*C2);
LPF_BPF = 1 / (1 + s*L2*R2);
BPF = HPF_BPF * LPF_BPF;
figure;
bode(BPF);
title('Bode Plot of Band-Pass Filter');
