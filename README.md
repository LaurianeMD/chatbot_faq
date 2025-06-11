# 🤖 Chatbot FAQ - Jumia Sénégal (Gradio) -App lien : https://chatbot-faq-tkmb.onrender.com

Ce projet est un **chatbot simple** qui permet aux utilisateurs de poser des **questions fréquentes** concernant les paiements sur Jumia Sénégal. Il utilise **Gradio** pour offrir une interface conviviale et est déployable en ligne via **Render**.

---

## 🎯 Fonctionnalités

- ✅ Répond automatiquement aux questions fréquentes à partir d'une base `faq.csv`
- ✅ Gère les **salutations**, **formules de politesse** ("comment ça va ?"), et **remerciements**
- ✅ Interface utilisateur web avec **Gradio**
- ✅ Prêt à être déployé sur **Render.com**

---

## 🗂️ Structure du projet

```bash
chatbot_faq/
├── faq.csv               # Questions/Réponses
├── model.py              # Moteur du chatbot (KNN + nettoyage)
├── gradio_app.py         # Interface Gradio
├── requirements.txt      # Dépendances Python
└── render.yaml           # Fichier de configuration pour Render
```

---

## 🚀 Lancer en local

### 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/chatbot-faq-gradio.git
cd chatbot-faq-gradio
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l'application Gradio

```bash
python gradio_app.py
```

L'application sera accessible sur :  
👉 http://127.0.0.1:7860

---

## 🌐 Déploiement sur Render

### Étapes :

1. Crée un compte sur https://render.com
2. Pousse ton code sur GitHub
3. Clique sur **"New Web Service"**
4. Choisis ton repo et laisse Render détecter automatiquement `render.yaml`
5. Ton app sera disponible à une URL publique comme :  
   `https://chatbot-faq-gradio.onrender.com`

---

## 💬 Exemples d'interactions

| Entrée utilisateur              | Réponse du chatbot                                                |
|---------------------------------|--------------------------------------------------------------------|
| Bonjour                         | Bonjour ! Comment puis-je vous aider ? 😊                         |
| Comment ça va ?                 | Je vais bien, merci ! Et vous ? 😊                                 |
| Merci beaucoup !                | Avec plaisir ! N'hésitez pas si vous avez d'autres questions. 🙏   |
| Quels modes de paiement existe ? | Jumia propose plusieurs options de paiement [...]                 |

---

## 📦 Fichier `requirements.txt`

```
gradio
pandas
scikit-learn
```

---

## ✍️ Auteur

Projet développé par **Lauriane MBAGDJE DORENAN**  

