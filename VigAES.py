import secrets
import io
import pyAesCrypt


# VIG

lettres = [chr(i) for i in range(ord('a'), ord('z')+1)]
valeurs = {lettre: i for i, lettre in enumerate(lettres)}
cle_vig = ["o", "u", "i"]  

def vig_encrypt(texte, cle):
    resultat = ""
    for i in range(len(texte)):
        lettre = texte[i].lower()
        if lettre in valeurs:
            v_texte = valeurs[lettre]
            v_cle = valeurs[cle[i % len(cle)]]
            v_chiffree = (v_texte + v_cle) % 26
            resultat += lettres[v_chiffree]
        else:
            resultat += lettre
    return resultat

def vig_decrypt(texte_chiffre, cle):
    resultat = ""
    for i in range(len(texte_chiffre)):
        lettre = texte_chiffre[i].lower()
        if lettre in valeurs:
            v_chiffree = valeurs[lettre]
            v_cle = valeurs[cle[i % len(cle)]]
            v_origine = (v_chiffree - v_cle) % 26
            resultat += lettres[v_origine]
        else:
            resultat += lettre
    return resultat


# AES 

BUFFER_SIZE = 64 * 1024  # 64 KB

def aes_encrypt(message: str) -> tuple[str, bytes]:
    key = secrets.token_hex(16) 
    fIn = io.BytesIO(message.encode("utf-8"))
    fOut = io.BytesIO()
    pyAesCrypt.encryptStream(fIn, fOut, key, BUFFER_SIZE)
    return key, fOut.getvalue()

def aes_decrypt(ciphertext: bytes, key: str) -> str:
    fIn = io.BytesIO(ciphertext)
    fOut = io.BytesIO()
    ct_len = len(ciphertext)
    origsize = ct_len - 16
    try:
        pyAesCrypt.decryptStream(fIn, fOut, key, BUFFER_SIZE, origsize)
        return fOut.getvalue().decode("utf-8")
    except Exception as e:
        return f"[ERREUR]: {e}"


# AES + Vig 

if __name__ == "__main__":
    message = input("Votre texte : ")
    print("Message original :", message)

    # Vig
    texte_vig = vig_encrypt(message, cle_vig)
    print("Après Vigenère :", texte_vig)

    # AES
    key_aes, ciphertext = aes_encrypt(texte_vig)
    print("\nClé AES :", key_aes)
    print("Ciphertext AES :", ciphertext[:60], "...")

    # decrypt AES
    recovered_vig = aes_decrypt(ciphertext, key_aes)
    print("\nAprès déchiffrement AES :", recovered_vig)

    # decrypt Vig
    recovered_message = vig_decrypt(recovered_vig, cle_vig)
    print("Message final déchiffré :", recovered_message)
