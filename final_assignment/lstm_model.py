import torch
import torch.nn as nn
import torch.nn.functional as F

class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size=6): # concatしたベクトル.sizeがinput_sizeに入ってくる batch_size
        super(LSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        out = F.softmax(out, dim=1)
        return out

class BiLSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size=6):
        super(BiLSTMModel, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        # Bidirectional LSTM
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, output_size) # 隠れ状態とセル状態のサイズを双方向用に2倍に

    def forward(self, input_ids, attention_mask):
        h0 = torch.zeros(self.num_layers * 2, input_ids.size(0), self.hidden_size).to(input_ids.device) # 双方向LSTMのため*2
        c0 = torch.zeros(self.num_layers * 2, input_ids.size(0), self.hidden_size).to(input_ids.device)
        
        out, _ = self.lstm(input_ids, (h0, c0))
        out = self.fc(out[:, -1, :])
        out = F.softmax(out, dim=1)            
        return out