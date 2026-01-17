import express from "express";
import * as dotenv from "dotenv";
import {createServer} from "node:http"

const PORT = process.env.PORT || 3000;
const app = express()

const server = createServer(app)


server.listen(PORT,()=>{
    console.log(`Server is running on ${PORT}`)
})
