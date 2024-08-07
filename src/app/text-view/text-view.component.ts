import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import axios from 'axios';

@Component({
  selector: 'app-text-view',
  templateUrl: './text-view.component.html',
  styleUrls: ['./text-view.component.css']
})
export class TextViewComponent {
  key: string = '';
  text: string = '';
  id: string;

  constructor(private route: ActivatedRoute) {
    this.id = this.route.snapshot.paramMap.get('id')!;
  }

  async fetchSnippet() {
    try {
      const response = await axios.post(`http://127.0.0.1:5000/api/view/${this.id}`, {
        key: this.key
      });
      this.text = response.data.text;
    } catch (error) {
      console.error('Error fetching snippet:', error);
    }
  }
}


