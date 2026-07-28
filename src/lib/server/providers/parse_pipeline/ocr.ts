import {createWorker} from 'tesseract.js';

async function extractText() {
    const worker = await createWorker('eng');
    const response = await worker.recognize('');
}

//wip