import torch
import bdh

# Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Same config used during training
config = bdh.BDHConfig(
    n_layer=3,
    n_embd=128,
    n_head=2,
)

# Load model
model = bdh.BDH(config).to(device)
model.load_state_dict(torch.load("bdh_weights.pt", map_location=device))
model.eval()

# Prompt
prompt_text = input("Enter prompt: ")
prompt = torch.tensor(
    bytearray(prompt_text, "utf-8"),
    dtype=torch.long,
    device=device
).unsqueeze(0)

# Generate
with torch.no_grad():
    output = model.generate(prompt, max_new_tokens=200, top_k=3)

# Decode
generated_text = bytes(
    output.squeeze(0).cpu().numpy().astype("uint8")
).decode(errors="ignore")

print("\nGenerated Text:\n")
print(generated_text)
