require('dotenv').config()
const express = require('express') // importation bibliothèque express 
const nodemailer = require('nodemailer') // importation bibliothèque express 
const cors = require('cors')
const app = express() // creation application Express, app est notre serveur web 
app.use(cors({
    origin: "http://localhost:5173", //autorise seulement le front-end 
    methods: ["GET", "POST", "OPTIONS"], // pour ces méthoddes
    allowedHeaders: ["Content-Type"], // autorise cet en-tete 
}))
app.use(express.json())

const port = 3000 // application accessible sur localhost://3000

app.get('/', (req, res) => { // quand qq fait une requete get sur "/" il obtient come reponse (res) Hello World
                             // req et res sont les objets requetes et reponse 
    res.send('Hello world')
})

// app.options('/email_sender', cors()) // enable pre-flight request for /email_sender route 
app.post('/email_sender', async(req, res) => {
    try {
    // -- Création du transport (SMTP transport) -- //
        const {text, html} = req.body // données envoyées via POST requete sont dans le req.body !!attention!! la j'ai mis les données en mode {text, html} mais du coup ca doit bien etre envoyé coté front-end sous format json (donc regarder coment bein envoyer les données)
//attention poour utiliser req.body il faut ajoputer app.use(express.json()) dans le serveur 
        console.log("données reçues : ", req.body)
        // const gmail_password = process.env.blacklist_gmail_password
        const gmail_password = process.env.BL_GMAIL_PASS

        const transporter = nodemailer.createTransport({
            host: "smtp.gmail.com", 
            port: 465, 
            secure: true, // true pour port 465 et faux pour les autres jsp pourquoi
            service: "gmail",
            auth: {
                user: "hh.blacklist@gmail.com", 
                pass: gmail_password
            }
        })



        await transporter.sendMail({
            from:"hh.blacklist@gmail.com", 
            to:"hh.blacklist@gmail.com", 
            subject:"New request for "+ req.body["institution_name"] + " from " + req.body["person_talking"], 
            // text:"Here are the information about the insitution request : ",
            html:`<p> Here are the information about the insitution request : </p> <br> <li> institution_name : ${req.body["institution_name"]} </li> <li> institution_location : ${req.body["institution_location"]} </li> <li> institution_postalCode : ${req.body["institution_postalCode"]} </li> <li> institution_mailAdress : ${req.body["institution_mailAdress"]} </li> <li> institution_director : ${req.body["institution_director"]} </li> <li> institution_phone : ${req.body["institution_phone"]} </li> <li> person_talking : ${req.body["person_talking"]} </li> <li> person_talking_role : ${req.body["person_talking_role"]} </li> <li> comment : ${req.body["comment"]} </li>`,
        })

        console.log("email envoyé")
        res.json({success:true, message:"email bien envoyé"})
    }
    catch (err) {
        console.error("erreur : ", err)
        res.status(500).json({success:false, error:err.message})
    }
})

app.listen(port, () => { // lance le server (quand on node app.js le server est lancé) et ecoute sur le port 
    console.log(`the app is running, listening on the port ${port}`) //log dans console terminal 
})