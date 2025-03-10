## 💻 System Requirements  

| 🚀 **Thread Count** | 🧠 **CPU (Cores/Threads)** | 💾 **RAM**      | 💽 **Disk (SSD/HDD)**          | 🌐 **Network Speed**   | 📝 **Notes**                                                   |
|------------------|--------------------------|-----------------|----------------------------|---------------------|-------------------------------------------------------------|
| **100**          | 🟢 4 cores / 8 threads     | 🟢 4GB           | 💿 SSD or HDD (No Heavy Load) | 📶 10-100 Mbps       | ✅ Low load, most systems can handle this with no issue.     |
| **250**          | 🟡 4-6 cores / 8-12 threads | 🟡 4-8GB         | 💿 SSD recommended          | 📶 50-100 Mbps       | ⚠️ Moderate load; SSD recommended for smooth operations.    |
| **500**          | 🟠 6-8 cores / 12 threads   | 🟠 8GB           | 💽 SSD strongly recommended  | 📶 100+ Mbps         | ⚠️ Heavy load, SSD needed for I/O speed, stable networking.  |
| **750**          | 🔴 8 cores / 16 threads     | 🔴 8-12GB        | 💽 SSD                      | 📶 100+ Mbps         | 📈 High thread count, decent network speed necessary.       |
| **1000**         | 🔥 8-12 cores / 16-24 threads | 🔥 12GB        | 💽 SSD                      | 🌐 1Gbps (Gigabit)   | 💪 High load, fast SSD + Gigabit network required.          |
| **1500**         | 🔥 12 cores / 24 threads    | 💪 16GB         | 💽 SSD                      | 🌐 1Gbps or higher   | 💥 Heavy processing, Potential discord rate limiting.       |
| **2000+**        | 💥 12-16 cores / 24-32 threads | 💥 16GB+    | 💽 SSD (Preferably NVMe)    | 🚀 1Gbps or higher   | 🧨 Extreme load, potential network bottlenecks, discord rate limits.|

---

## 🍓 Running on a Raspberry Pi / SBC  

If you're planning to run this on a **Raspberry Pi** or any other **Single Board Computer (SBC)**, here are the recommended specifications:  

| ⚙️ **Thread Count** | 💾 **Recommended RAM** | 📝 **Notes**                |
|------------------|------------------------|---------------------------|
| **10**           | 1 / 2 GB                | ✅ 2GB Recommended.        |
| **50**           | 2 / 4 GB                | ✅ 4GB Recommended.        |
| **100**          | 4 / 8 GB                | ✅ 8GB Recommended.        |
| **200+**         | 8+ GB                   | 💥 Anything above 8GB.     |

For **best performance**, I recommend using an SBC with **8GB+ RAM** and keeping it online for as long as possible. The longer it's up, the more images it pulls.  

---

## 💡 My Personal Setup  

For reference, I personally run this project on my **desktop PC** with the following specs:  
- **💻 CPU:** Ryzen 5 4600G (not the best, but does the job)  
- **💾 RAM:** 16GB  
- **💽 Disk:** SSD  
- **GPU:** ❌ Doesn't matter (no GPU acceleration yet)  

I can comfortably push **3000 threads** with this setup. 🚀  


## 📝 NOTES

This **Will** eat up your storage if you enable saving in the config file. Please ensure you have enough disk space or disable saving.<br>
All images will be downloaded to wherever you put this script, so if you have a second drive you want to save images to, put the script on it.