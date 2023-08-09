import express from 'express'
import cors from 'cors'
import {data} from '../api/news.mjs'

const app = express();
app.use(express.json());
app.use(cors());

app.get("/" ,(req , res) =>{
    res.status(200).json(data)
} )

app.listen(4000);