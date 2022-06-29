***********************
Accounting and Pricing
***********************

.. sectionauthor:: Eric Yen <Eric.Yen@twgrid.org>, Mike Yang <mike.yang@twgrid.org>

----------------------------
Accounting Information
----------------------------

Monthly Accounting
^^^^^^^^^^^^^^^^^^^^

The monthly accounting will be calculated and formatted as a bill in group basis. The group PI will receieve the bill and accounting report by the 15th of next month. The accounting bill is also viewable in the DiCOS web.

Accounting/Usage Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are arranging for some dashboard for user's accounting information and the usage of the resources. Please wait for the dashboard. Thank you.

-------------------------------------------
Accounting Regulations
-------------------------------------------

ASGC 研究型服務收費 (ASGC Pricing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**物理所⾼能物理與科學計算中⼼** (簡稱 **科學計算中⼼** 或 **ASGC**) 與院內研究團隊合作，⽀援⼤數據分析與科學計算等需求。依據使⽤者付費與永續發展策略，收費內容包含計算服務、儲存服務、以及系統開發與維運三項。計算服務以 Standard Resource Unit (SRU) 為單位計算使⽤費。SRU 為計算系統依其效能加權後計算設備使⽤量的單位。儲存服務每⽉以實際使⽤過的最⼤空間計算，逐⽉合計。系統開發與維運為需額外軟體系統或服務開發之需求，以⼈時為單位計算。計費模式彙整如表一。各計算系統每⼆⼗四⼩時使⽤單價 (以 CPUCore-Day 或 GPUBoard-Day 計算) 如表⼆。本中⼼每⽉寄送使⽤統計與預估費⽤予各 PI。實際應付費⽤為使⽤費 (計算、儲存與開發總和) 減去扣減額。扣減額則包含院⽅補助本中⼼費⽤，以及合作研究團隊提供之經費或設備。使⽤費可以年度繳付，或於帳號結束時繳付。繳付⽅式請依院內規定辦理，憑本中⼼開立之使⽤費通知，於次年⼀⽉經院內預算系統轉帳予本中⼼。院外使⽤者則請透過電匯、⽀票或到院繳付等⽅式付款。 


.. list-table:: 表一：本表說明物理所⾼能物理與科學計算中⼼研究服務計費模式
   :header-rows: 1

   * - 研究服務項⽬
     - 計費模式 (院內使⽤者)
   * - 計算服務
     - 各系統依效能正規化後之 SRU 為單位計費。1 SRU = NTD$3
   * - 儲存服務
     - 1,000NTD/TB-Year
   * - 系統開發與維運
     - 基本維運成本均已列入計價模式。額外需開發之軟體、系統或使⽤介⾯等，將另按⼯時計費
   * - 資料傳輸
     - ⽬前未納入計費

.. note::

   1. 計算服務使⽤費計算⽅式為 SRU ⽤量 x 3 (1 SRU = NTD$3)。SRU ⽤量為 CPUCore-Day 或 GPUBoard-Day 乘上系統權值
   2. 基本維運包含穩定性、資安、系統更新與系統效能調校等，均已列入計價模式中，不另外計費
   3. 如需額外軟體系統或服務開發，將再另以 50,000 NTD / 160 Work-Hr 為單位計費，或由需求單位提供⼈員費⽤。所聘⽤⼈⼒均由 ASGC 統⼀調度管理
   4. ⾃⾏提供設備或設備費，併入網格中⼼共享資源者，該單位使⽤費將可扣減(每年扣除該設 備購置費⽤五分之⼀)。且提供單位有該設備優先使⽤權
   5. 此計費辦法將每年與使⽤社群討論更新


中研院冷凍電顯大數據分析與資料儲存資源使用說明 (ASCEM‐ASGC Big Data Analysis Resource Usage for CryoEM Data Storage and Computing)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本院冷凍電顯核心設施與網格中心 (ASGC) 合作提供冷凍電顯設施使用者穩定且高效能的大數據處理與運算資源。依據研究需求，客製化從取得數據到完成分析與資料備份保存整體資料處理流程，如同使用專屬設施般，便利的使用 CryoSparc, Relion, CisTEM, JupyterLab 等工具，於整合的高效能雲端計算與儲存資源完成所需分析。使用者可依據需要選擇分析環境與不同效能的 GPU (V100, 3090, P100) 或 CPU 計算資源。每位使用者於計算環境中可使用最大儲存空間為 60TB，另並提供預設儲存二份的備份與長期保存空間。 為維持整體雲端系統的穩定與效能，計算與儲存資源均依據用量列計使用費，每年一月需繳付前一年的使用費。所收取費用均優先改善冷凍電顯大數據分析資源與效能。冷凍電顯計算與儲存資源之管理均以群組為單位，PI 為該群組負責人。各群組間資料均獨立。網格中心每月將提供每位主持人前一月份的使用量與費用報表，並於每年一月寄送繳費通知。服務內容與計費模式均將透過冷凍電顯定期的使用者委員會議中，持續檢討改善。 使用運算資源者，應於學術發表中致謝 TPP、ASCEM、及 ASGC。 使用帳號申請、計費模式、服務內容以及任何問題與建議，均請參見網格中心網站，或逕與網格中心聯繫。

ASGC provides big data computing and storage resource and services for ASCEM users in collaboration with ASCEM. According to the research needs, customized data analysis pipeline is provisioned over the science cloud integrating high-performance GPU, CPU clusters as well as data storage system. CryoSparc, Relion, CisTEM, and JupyterLab are all available over the cloud right as dedicated computing environment. User could choose a variety of GPU or CPU resource for his analysis based on performance requirements. Each user account has 60TB disk space quota. Services for backup and long-term storage with two-copy by default are also provided. In order to maintain the reliability and efficiency of the ASCEM computing system evolutionarily, resource usage fee is a must according to the consumption. Resource usage fee is paid based on PI group annually in January. These payment will be used to enhance the reliability and efficiency of ASCEM computing system precedently. Monthly accounting report will be delivered to each PI including usage of every member account. Any improvement of the services, pricing model and resource policy will be discussed in regular ASCEM User Committee meeting. In addition to ASCEM (Academia Sinica Cryo-EM Facility) and TPP (Taiwan Protein Project (Grant No. AS-KPQ-109-TPP2)), please also include ASGC (Academia Sinica Grid-computing Center) in the acknowledgement when research outcomes that relied on ASGC resources, services or expertise are presented in your research. User account application, pricing model, services and any comment or question, please refer to ASGC web site or contact ASGC directly. 

---------------
Pricing Rate
---------------

Computing Resource (CE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

本表各系統每⼆⼗四⼩時使⽤量之單價（以 CPUCore-Day 或 GPUBoard-Day 計算)。
(Last Updated: Feb. 2022. Pricing model will be reviewed and revised annually.)

Computing Pricing (1 SRU = NTD$3)         

.. list-table:: 表二a：ASGC CE Pricing 2022 Feb.
   :header-rows: 1

   * - Model
     - Type
     - Price (CPU Core/GPU Board/Day in NT$)
   * - FDR5
     - CPU
     - 1.2
   * - FDR4
     - CPU
     - 1
   * - QDR4
     - CPU
     - 0.75
   * - QDR2
     - CPU
     - 0.65
   * - GTX-1080Ti
     - GPU
     - 5
   * - RTX3090
     - GPU
     - 395
   * - P100
     - GPU
     - 235
   * - V100
     - GPU
     - 350
   * - A100
     - GPU
     - 865

Storage Resource (SE)
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 表二b：ASGC SE Pricing 2022 Feb.
   :header-rows: 1

   * - Storage
     - Price (TB/year in NT$)
   * - Storage
     - 1000

Power Consumpution
^^^^^^^^^^^^^^^^^^^^^^^

TBD



