def cleandf(df,tdv):

    df_add = pd.DataFrame(columns=df.columns)
    df['Created Date']=pd.to_datetime(df['Created Date'])
    df = df[df['Created Date']>tdv].copy()
    for i in range(0, len(df['Email'])): 
        if df['Email'][i] == '(not shared)':
            df.loc[i, 'Email'] = df['Reward Email'][i]
      
    for j in range(0, len(df['Email'])):
        if not pd.isna(df['Reward Email'][j]):
            if df['Reward Email'][j].lower() != df['Email'][j].lower():
                addval = df.iloc[[j]].copy()
                addval['Email'] = addval['Reward Email']
                df_add = pd.concat([df_add,addval],axis = 0)
                
    df_res = pd.concat([df,df_add],axis = 0)
    df_res = df_res[df_res['Email'].notna()]
    df_res = df_res.reset_index()

    if 'Amount (May be approx.) (PC)' in df_res.columns:
        temp_df = df_res
        df_vip = temp_df[temp_df['Amount (May be approx.) (PC)'] > 250]
        df_normal = temp_df[temp_df['Amount (May be approx.) (PC)'] <= 250]
        
    else:
        temp_df = df_res
        df_vip = temp_df[temp_df['Amount (PC)'] > 250]
        df_normal = temp_df[temp_df['Amount (PC)'] <= 250]
        
    return df_vip,df_normal